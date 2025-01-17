from functools import lru_cache
import bisect

from experta.abstract import Strategy


class DepthStrategy(Strategy):
    @lru_cache()
    def get_key(self, activation):
        salience = activation.rule.salience
        facts = sorted((f['__factid__'] for f in activation.facts),
                       reverse=True)
        return (salience, facts)

    def _update_agenda(self, agenda, added, removed):
        for act in removed:
            act.key = self.get_key(act)
            idx = bisect.bisect_left(agenda.activations, act)
            for o in (0, 1, -1):
                try:
                    if agenda.activations[idx+o] == act:
                        del agenda.activations[idx+o]
                    else:
                        continue
                except IndexError:
                    pass
                else:
                    break

        for act in added:
            act.key = self.get_key(act)
            bisect.insort(agenda.activations, act)
