# SPDX-FileCopyrightText: © 2023 Uri Shaked <uri@tinytapeout.com>
# SPDX-License-Identifier: MIT

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles
import random

# DMADD madd(
        # .clk    (clk),
        # .run    (uio_in[3]),
        # .load   (uio_in[2]),
        # .insn   (uio_in[1:0]),
        # .index  (ui_in[7:4]),
        # .data   (ui_in[3:0]),
        # .out    ({uio_out[7:4],uo_out}),
        # .rst_n  (rst_n)
# );

@cocotb.test()
async def test_mn1(dut):
    dut._log.info("min 1")
  
    # Our example module doesn't use clock and reset, but we show how to use them here anyway.
    clock = Clock(dut.clk, 20, units="us")
    cocotb.start_soon(clock.start())
    dut.rst_n.value = 0
    dut.uio_in.value = 0b0000_0_0_00
    await ClockCycles(dut.clk,10)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk,10)
    dut.ena.value  = 1
    dut.uio_in.value = 0b0000_0_1_00
    dut.ui_in.value = 0b0001_0000
    await ClockCycles(dut.clk,1 )
    dut.uio_in.value  = 0b0000_1_0_00
    await ClockCycles(dut.clk,30 )
    dut._log.info(dut.uo_out.value)
    assert dut.uo_out.value==1

@cocotb.test()
async def test_mn12(dut):
    dut._log.info("min 12")
  
    # Our example module doesn't use clock and reset, but we show how to use them here anyway.
    clock = Clock(dut.clk, 20, units="ns")
    cocotb.start_soon(clock.start())
    dut.rst_n.value = 0
    dut.uio_in.value = 0b0000_0_0_00
    await ClockCycles(dut.clk,10)
    dut.rst_n.value = 1
    dut.ena.value = 1
    dut.uio_in.value = 0b0000_0_1_00
    dut.ui_in.value = 0b1100_0000
    await ClockCycles(dut.clk,1 )
    dut.uio_in.value = 0b0000_1_0_00
    await ClockCycles(dut.clk,20 )
    dut._log.info(dut.uo_out.value)
    assert dut.uo_out.value == 12

@cocotb.test()
async def test_mn78(dut):
    dut._log.info("min 78")
  
    # Our example module doesn't use clock and reset, but we show how to use them here anyway.
    
    clock = Clock(dut.clk, 20, units="ns")
    cocotb.start_soon(clock.start())
    await ClockCycles(dut.clk,10)
    dut.rst_n.value = 0
    dut.uio_in.value = 0b0000_0_0_00
    await ClockCycles(dut.clk,10)
    # Reset
    dut.ena.value = 1
    dut.rst_n.value = 1
    await ClockCycles(dut.clk,1)
    dut.uio_in.value = 0b0000_0_1_00
    dut.ui_in.value = 0b0111_0000
    await ClockCycles(dut.clk,1 )
    dut.ui_in.value = 0b1000_0000
    await ClockCycles(dut.clk,1 )
    dut.uio_in.value = 0b0000_1_0_00
    await ClockCycles(dut.clk,30 )
    dut._log.info(dut.uo_out.value)
    assert dut.uo_out.value==7
 
@cocotb.test()
async def test_mn8(dut):
    dut._log.info("min 8")
  
    # Our example module doesn't use clock and reset, but we show how to use them here anyway.
    
    clock = Clock(dut.clk, 20, units="ns")
    cocotb.start_soon(clock.start())

    dut.rst_n.value = 0
    await ClockCycles(dut.clk,10)
    # Reset
    dut.ena.value = 1
    dut.rst_n.value = 1
    dut.uio_in.value = 0b0000_0_1_00
    dut.ui_in.value = 0b1000_0000
    await ClockCycles(dut.clk,10 )
    dut.uio_in.value = 0b0000_1_0_00
    await ClockCycles(dut.clk,30 )
    dut._log.info(dut.uo_out.value)
    assert dut.uo_out.value==8
# 
# #
# # #######################################
# #
# 
@cocotb.test()
async def test_mx1(dut):
    dut._log.info("max 1")
  
    # Our example module doesn't use clock and reset, but we show how to use them here anyway.
    clock = Clock(dut.clk, 20, units="ns")
    cocotb.start_soon(clock.start())
    dut.rst_n.value = 0
    dut.uio_in.value = 0b0000_0_0_00
    await ClockCycles(dut.clk,10)
    dut.rst_n.value = 1
    await ClockCycles(dut.clk,1)
    dut.ena.value = 1
    dut.uio_in.value = 0b0000_0_1_01
    dut.ui_in.value = 0b0001_0000
    await ClockCycles(dut.clk,1 )
    dut.uio_in.value = 0b0000_1_0_01
    await ClockCycles(dut.clk,30 )
    dut._log.info(dut.uo_out.value)
    assert dut.uo_out.value==1

@cocotb.test()
async def test_mx12(dut):
    dut._log.info("max 12")
  
    # Our example module doesn't use clock and reset, but we show how to use them here anyway.
    clock = Clock(dut.clk, 20, units="ns")
    cocotb.start_soon(clock.start())
    dut.rst_n.value = 0
    dut.uio_in.value = 0b0000_0_0_00
    await ClockCycles(dut.clk,10)
    dut.rst_n.value = 1
    dut.ena.value = 1
    dut.uio_in.value = 0b0000_0_1_01
    dut.ui_in.value = 0b1100_0000
    await ClockCycles(dut.clk,1 )
    dut.uio_in.value = 0b0000_1_0_01
    await ClockCycles(dut.clk,20 )
    dut._log.info(dut.uo_out.value)
    assert dut.uo_out.value==12

@cocotb.test()
async def test_mx78(dut):
    dut._log.info("max 78")
  
    # Our example module doesn't use clock and reset, but we show how to use them here anyway.
    
    clock = Clock(dut.clk, 20, units="ns")
    cocotb.start_soon(clock.start())
    dut.rst_n.value = 0
    dut.uio_in.value = 0b0000_0_0_00
    await ClockCycles(dut.clk,10)
    # Reset
    dut.ena.value = 1
    dut.rst_n.value = 1
    dut.uio_in.value = 0b0000_0_1_01
    dut.ui_in.value = 0b0111_0000
    await ClockCycles(dut.clk,1 )
    dut.ui_in.value = 0b1000_0000
    await ClockCycles(dut.clk,1 )
    dut.uio_in.value = 0b0000_1_0_01
    await ClockCycles(dut.clk,20)
    dut._log.info(dut.uo_out.value)
    assert dut.uo_out.value==8

@cocotb.test()
async def test_mx8(dut):
    dut._log.info("max 1")
  
    # Our example module doesn't use clock and reset, but we show how to use them here anyway.
    
    clock = Clock(dut.clk, 20, units="ns")
    cocotb.start_soon(clock.start())
    dut.rst_n.value = 0
    dut.uio_in.value = 0b0000_0_0_00
    await ClockCycles(dut.clk,10)
    # Reset
    dut.ena.value = 1
    dut.rst_n.value = 1
    dut.uio_in.value = 0b0000_0_1_01
    dut.ui_in.value = 0b0001_0000
    await ClockCycles(dut.clk,1 )
    dut.uio_in.value = 0b0000_1_0_01
    await ClockCycles(dut.clk,20)
    dut._log.info(dut.uo_out.value)
    assert dut.uo_out.value== 1

####################################################

@cocotb.test()
async def test_madd1(dut):
    dut._log.info("max 7*1 + 5*3")
  
    # Our example module doesn't use clock and reset, but we show how to use them here anyway.
    
    clock = Clock(dut.clk, 20, units="ns")
    cocotb.start_soon(clock.start())
    dut.rst_n.value = 0
    dut.uio_in.value = 0b0000_0_0_00
    await ClockCycles(dut.clk,10)
    # Reset
    dut.ena.value = 1
    dut.rst_n.value= 1
    dut.uio_in.value = 0b0000_0_1_10
    dut.ui_in.value = 0b0111_0001
    await ClockCycles(dut.clk,1 )
    dut.ui_in.value = 0b0011_0101
    await ClockCycles(dut.clk,1 )
    
    dut.uio_in.value = 0b0000_1_0_10
    await ClockCycles(dut.clk,20)
    dut._log.info(dut.uo_out.value)
    assert dut.uo_out.value== 22


@cocotb.test()
async def test_madd2(dut):
    dut._log.info("max 1*1 + 15*1")
  
    # Our example module doesn't use clock and reset, but we show how to use them here anyway.
    
    clock = Clock(dut.clk, 20, units="ns")
    cocotb.start_soon(clock.start())
    dut.rst_n.value = 0
    dut.uio_in.value = 0b0000_0_0_00
    await ClockCycles(dut.clk,10)
    # Reset
    dut.ena.value = 1
    dut.rst_n.value = 1
    dut.uio_in.value = 0b0000_0_1_10
    dut.ui_in.value = 0b1110_0001
    await ClockCycles(dut.clk,1 )
    dut.ui_in.value = 0b0001_0010
    await ClockCycles(dut.clk,1 )
    
    dut.uio_in.value = 0b0000_1_0_10
    await ClockCycles(dut.clk,20)
    dut._log.info(dut.uo_out.value)
    assert dut.uo_out.value== 16


@cocotb.test()
async def test_madd_full(dut):
    dut._log.info("a n num value dot product")
  
    # Our example module doesn't use clock and reset, but we show how to use them here anyway.
    
    clock = Clock(dut.clk, 20, units="ns")
    cocotb.start_soon(clock.start())
    dut.rst_n.value = 0
    dut.uio_in.value = 0b0000_0_0_00
    await ClockCycles(dut.clk,10)
    # Reset
    dut.ena.value = 1
    dut.rst_n.value= 1
    dot = 0 
    for _ in range(50):
        w = random.randint(0,5)
        i = random.randint(0,5)
        v = (w<<4)+i
        dot += w * i 
        dut.uio_in.value = 0b0000_0_1_10
        dut.ui_in.value = v
        await ClockCycles(dut.clk,1 )
    dut.uio_in.value = 0b0000_1_0_10
    await ClockCycles(dut.clk,20)
    dut._log.info(dot)
    dut._log.info(int(dut.uo_out.value))
    dut._log.info(int(dut.uio_out.value))
    out_val = dut.uio_out.value<<4 | dut.uo_out.value
    assert out_val == dot
