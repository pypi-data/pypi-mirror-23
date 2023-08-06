-------------------------------------------------------------------------------
-- File       : tb_division.vhd
-------------------------------------------------------------------------------

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

entity tb_division is
end tb_division;

architecture behaviour of tb_division is

	------------------------------------------------------------------------------
	-- CONSTANTS DECLARATION
	------------------------------------------------------------------------------
	constant C_SIGNED_MODE: boolean   := True;  -- true
	constant C_WORD_WIDTH : integer   := 8;
	constant C_VCC        : std_logic := '1';
	constant C_GND        : std_logic := '0';

	------------------------------------------------------------------------------
	-- SIGNALS DECLARATION
	------------------------------------------------------------------------------
	signal dut_rst          : std_logic := C_VCC;                                 -- DUT - Asynchronous reset
	signal dut_rst_meta     : std_logic;                                          -- DUT - metastable  reset  
	signal dut_rst_sync     : std_logic;                                          -- DUT - synchronous reset
	signal dut_clk          : std_logic := C_GND;                                 -- DUT - clock, positive edge trigger
	signal dut_en           : std_logic;                                          -- DUT - Enable global signal
	signal dut_ope_en       : std_logic;                                          -- DUT - Operand Enable
	signal dut_ope_dividend : std_logic_vector(C_WORD_WIDTH-1 downto 0);          -- DUT - Operand Dividend
	signal dut_ope_divisor  : std_logic_vector(C_WORD_WIDTH-1 downto 0);          -- DUT - Operand Divisor
	signal dut_res_en       : std_logic;                                          -- DUT - Result Enable 
	signal dut_res_quotient : std_logic_vector(C_WORD_WIDTH-1 downto 0);          -- DUT - Result Quotient
	signal dut_res_remainder: std_logic_vector(C_WORD_WIDTH-1 downto 0);          -- DUT - Result remainder


	signal chk_res_quotient : std_logic_vector(C_WORD_WIDTH-1 downto 0);
	signal chk_res_remainder: std_logic_vector(C_WORD_WIDTH-1 downto 0);  

	-- Add user signal here
	signal TestIndex  : natural := 0;
	signal CheckIndex : natural := 0;
	signal ClkCnt     : natural:= 0;

	type TestArray is array (natural range <>) of integer;
	constant DividendArray  : TestArray := (13, 13, -13, -13, -13);
	constant DivisorArray   : TestArray := (3,  -3,   3,  -3,  -3);
	constant QuotientArray  : TestArray := (4,  -4,  -4,   4,   4);
	constant RemainderArray : TestArray := (1,   1,  -1,  -1,  -1);

begin  -- behaviour

	------------------------------------------------------------------------------
	-- GLOBAL SIGNAL GENERATION
	------------------------------------------------------------------------------
	-- Generation of Reset
	proc_rst:
	process
	begin
		dut_rst <= '1';
		wait for 1 us;
		dut_rst <= '0';
		wait;
	end process;

	-- Clock generated at 100Mhz
	proc_clk:
	process
	begin
		wait for 5 ns;
		dut_clk <= not(dut_clk);
	end process;

	-- Generation of Clear  
	--   Complete this process:
	--   * Use the dut_rst_meta signal to prevent the dut_rst_sync of metastable state
	--   * Reset value is C_VCC (Active High)
	--   * Use C_GND value to disable the reset 
	proc_clr:
	process(dut_rst, dut_clk)
	begin
		if dut_rst = '1' then
			dut_rst_meta <= C_VCC;
			dut_rst_sync <= C_VCC;
		elsif rising_edge(dut_clk) then
			dut_rst_meta <= C_GND;
			dut_rst_sync <= dut_rst_meta;

		end if;
	end process;

	-- Generation of Enable  
	proc_en:
	process(dut_rst, dut_clk)
	begin
		if dut_rst = '1' then
		  dut_en <= '0';
		elsif rising_edge(dut_clk) then
		  dut_en <= not(dut_rst_sync);
		end if;
	end process;


	------------------------------------------------------------------------------
	-- Design Under Test
	------------------------------------------------------------------------------
	inst_dut_division: entity work.division(rtl) 
	generic map(
		C_SIGNED_MODE=> C_SIGNED_MODE,
		C_WORD_WIDTH => C_WORD_WIDTH)
	port map(
		-- Global Signals
		rst           => dut_rst_sync,                                              -- [in ] Asynchronous reset
		clr           => C_GND,                                                     -- [in ] synchronous reset
		clk           => dut_clk,                                                   -- [in ] clock, positive edge trigger
		en            => dut_en,                                                    -- [in ] Enable global signal
		--Input operands
		ope_en        => dut_ope_en,                                                -- [in ] Operand Enable
		ope_dividend  => dut_ope_dividend,                                          -- [in ] Operand Dividend
		ope_divisor   => dut_ope_divisor,                                           -- [in ] Operand Divisor
		--Outpout results
		res_en        => dut_res_en,                                                -- [out] Result Enable 
		res_quotient  => dut_res_quotient,                                          -- [out] Result Quotient
		res_remainder => dut_res_remainder);                                        -- [out] Result remainder


	------------------------------------------------------------------------------
	-- Input Operand Generation
	------------------------------------------------------------------------------
	-- Complete this process to check of the possible division
	-- dut_ope_dividend range : 0x00 to 0xFF
	-- dut_ope_divisor range : 0x01 to 0xFF
	------------------------------------------------------------------------------
	proc_gen_operands:
	process(dut_rst, dut_clk)
	begin
		if dut_rst_sync = '1' then
			ClkCnt <= 4;
			TestIndex<=0;
			dut_ope_en <= '0';
			dut_ope_dividend <= (others=>'0');
			dut_ope_divisor  <= (others=>'0');
		elsif rising_edge(dut_clk) then      
			if ClkCnt=0 then 
				if TestIndex>=(DividendArray'length-1) then
					ClkCnt <= 100;
				else
					ClkCnt <= C_WORD_WIDTH+4;
				end if;
				dut_ope_en <= '1';
				dut_ope_dividend <= STD_LOGIC_VECTOR(TO_SIGNED(DividendArray(TestIndex), C_WORD_WIDTH));
				dut_ope_divisor  <= STD_LOGIC_VECTOR(TO_SIGNED(DivisorArray(TestIndex), C_WORD_WIDTH));
				TestIndex <= TestIndex+1;
			else
				ClkCnt <= ClkCnt-1;
				dut_ope_en <= '0';
			end if;
		end if;
	end process;

	------------------------------------------------------------------------------
	-- Output Results Checker
	------------------------------------------------------------------------------
	proc_chk_results:
	process(dut_rst, dut_clk)
	begin
		if dut_rst = '1' then
			CheckIndex<=0;
		elsif rising_edge(dut_clk) then
			if dut_res_en='1' then
				CheckIndex <= CheckIndex+1;
				if dut_res_quotient/=chk_res_quotient then 
					assert false report "Quotient does not match expected." severity failure;
				elsif dut_res_remainder/=chk_res_remainder then
					assert false report "Remainder does not match expected." severity failure;
				end if;
				if CheckIndex>=(DividendArray'length-1) then
					assert false report "Testbench completed." severity failure;
				end if;
			end if;
		end if;
	end process;
	
	chk_res_quotient  <= STD_LOGIC_VECTOR(TO_SIGNED(QuotientArray(CheckIndex), C_WORD_WIDTH));
	chk_res_remainder <= STD_LOGIC_VECTOR(TO_SIGNED(RemainderArray(CheckIndex), C_WORD_WIDTH));

end behaviour;

