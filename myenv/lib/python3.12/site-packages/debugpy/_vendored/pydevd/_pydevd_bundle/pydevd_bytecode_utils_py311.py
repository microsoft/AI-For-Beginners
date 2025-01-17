from _pydevd_bundle.pydevd_constants import IS_PY311_OR_GREATER
import dis
from types import CodeType
from collections import namedtuple

DEBUG = False

_Pos = namedtuple("_Pos", "lineno endlineno startcol endcol")


def _is_inside(item_pos: _Pos, container_pos: _Pos):
    if item_pos.lineno < container_pos.lineno or item_pos.endlineno > container_pos.endlineno:
        return False

    if item_pos.lineno == container_pos.lineno:
        if item_pos.startcol < container_pos.startcol:
            return False

    if item_pos.endlineno == container_pos.endlineno:
        if item_pos.endcol > container_pos.endcol:
            return False

    # Not outside, must be inside.
    return True


def _get_smart_step_into_targets(code):
    import linecache
    from .pydevd_bytecode_utils import Target

    filename = code.co_filename

    targets_root = []
    children = []
    for instr in dis.Bytecode(code):
        if instr.opname == "LOAD_CONST":
            if isinstance(instr.argval, CodeType):
                children.append(_get_smart_step_into_targets(instr.argval))

        elif instr.opname in ("CALL", "CALL_INTRINSIC_1"):
            positions = instr.positions
            if positions.lineno is None:
                continue
            if positions.end_lineno is None:
                continue
            lines = []
            for lineno in range(positions.lineno, positions.end_lineno + 1):
                lines.append(linecache.getline(filename, lineno))

            startcol = positions.col_offset
            endcol = positions.end_col_offset

            if positions.lineno == positions.end_lineno:
                lines[0] = lines[0][startcol:endcol]
            else:
                lines[0] = lines[0][startcol:]
                lines[-1] = lines[-1][:endcol]

            pos = _Pos(positions.lineno, positions.end_lineno, startcol, endcol)
            targets_root.append(Target("".join(lines), positions.lineno, instr.offset, [], positions.end_lineno, startcol, endcol))

    for targets in children:
        for child_target in targets:
            pos = _Pos(child_target.lineno, child_target.endlineno, child_target.startcol, child_target.endcol)

            for outer_target in targets_root:
                outer_pos = _Pos(outer_target.lineno, outer_target.endlineno, outer_target.startcol, outer_target.endcol)
                if _is_inside(pos, outer_pos):
                    outer_target.children_targets.append(child_target)
                    break
    return targets_root


def calculate_smart_step_into_variants(frame, start_line, end_line, base=0):
    """
    Calculate smart step into variants for the given line range.
    :param frame:
    :type frame: :py:class:`types.FrameType`
    :param start_line:
    :param end_line:
    :return: A list of call names from the first to the last.
    :note: it's guaranteed that the offsets appear in order.
    :raise: :py:class:`RuntimeError` if failed to parse the bytecode or if dis cannot be used.
    """
    from .pydevd_bytecode_utils import _convert_target_to_variant

    variants = []
    code = frame.f_code
    lasti = frame.f_lasti

    call_order_cache = {}
    if DEBUG:
        print("dis.dis:")
        if IS_PY311_OR_GREATER:
            dis.dis(code, show_caches=False)
        else:
            dis.dis(code)

    for target in _get_smart_step_into_targets(code):
        variant = _convert_target_to_variant(target, start_line, end_line, call_order_cache, lasti, base)
        if variant is None:
            continue
        variants.append(variant)

    return variants
