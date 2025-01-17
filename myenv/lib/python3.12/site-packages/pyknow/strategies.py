from functools import lru_cache
import bisect

from pyknow.abstract import Strategy


class DepthStrategy(Strategy):
    @lru_cache()
    def get_key(self, activation):
        salience = activation.rule.salience
        facts = sorted((f['__factid__'] for f in activation.facts),
                       reverse=True)
        return (salience, facts)

    def _update_agenda(self, agenda, added, removed):
        for act in added:
            act.key = self.get_key(act)
            bisect.insort_left(agenda.activations, act)

        for act in removed:
            try:
                act.key = self.get_key(act)
                idx = bisect.bisect_left(agenda.activations, act)
                if agenda.activations[idx] == act:
                    del agenda.activations[idx]
                elif agenda.activations[idx + 1] == act:
                    del agenda.activations[idx + 1]
            except IndexError:
                # Already executed rule.
                pass
