
import zuspec.dataclasses as zdc

@zdc.dataclass
class WishboneInitiator(zdc.Bundle):
    DATA_WIDTH : zdc.u32 = zdc.const(default=32)
    ADDR_WIDTH : zdc.u32 = zdc.const(default=32)
    adr : zdc.bitv = zdc.output(width=lambda s:s.ADDR_WIDTH)
    dat_w : zdc.bitv = zdc.output(width=lambda s:s.DATA_WIDTH)
    dat_r : zdc.bitv = zdc.input(width=lambda s:s.DATA_WIDTH)
    cyc : zdc.bit = zdc.output()
    err : zdc.bit = zdc.input()
    sel : zdc.bitv = zdc.input(width=lambda s:int(s.DATA_WIDTH/8))
    ack : zdc.bit = zdc.input()
    we : zdc.bit = zdc.output()
