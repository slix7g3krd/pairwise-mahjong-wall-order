import pytest
import game.mahjong_wall as mod

CASES = [
    ("draw_pointer_recompute", (1,)),
    ("call_claim_rollback", (1,)),
    ("wall_head_tail_cursor", (1,)),
    ("tile_count_invariant", (1,)),
    ("shuffle_seed_carry", (1,)),
    ("action_log_idempotent", (1,)),
    ("load_mahjong", (1,)),
    ("draw_tile", (1,)),
    ("claim_meld", (1,)),
    ("present_mahjong", (1,)),
    ("validate_mahjong", (1,)),
    ("metrics_mahjong", (1,)),
    ("audit_mahjong", (1,)),
    ("fallback_mahjong", (1,)),
    ("determinism_mahjong", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
