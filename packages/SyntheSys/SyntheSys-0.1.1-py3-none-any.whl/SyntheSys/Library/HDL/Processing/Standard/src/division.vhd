-------------------------------------------------------------------------------
-- File       : division.vhd
-------------------------------------------------------------------------------

library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

--generic division Module
--  Division with unsigned/signed operands
--  This entity is a unsigned or signed binary division which is using the 
--  Restoring Division Algorithm.
--
--      x = qd + rem

--          x: Dividend
--          q: quotient
--          d: divisor
--          rem: remainder
--
--  Set x in register A, d in register B, 0 in register P, and 
--  perform n divide steps (n is the quotient wordlength)
--      Each step consists of:
--          1-Shift the register pair (P,A) one bit left
--          2-Subtract the contents of B from P, put the result back in P
--          3-If the result is < 0 (i.e. P<B) , set the low-order bit of A to 0 otherwise to 1
--          4-If the result is < 0, restore the old value of P otherswise store the result of subsract
--
--  The Dividend and the divisor have to be stable when the operand
--  enable input is set to high for at least 1 clock period of clk to
--  be stored inr registers.
--  The division operation is performed during C_WORD_WIDTH clock
--  periods once operand enable signal is released and drive to LOW.
--  The quotient and the remainder of the division will be issued by
--  the module when result enable signal is set to HIGH during one clock.
--  The quotient and the remainder will stay stable until next result
--  is issued.
--  The total process (i.e load, division operation, issue of results)
--  is performed in C_WORD_WIDTH+2 clock periods of clock

entity division is  
	generic (
		C_SIGNED_MODE : boolean := true;                                            -- Signed Mode configuration of division module
		C_WORD_WIDTH  : integer := 32);                                             -- Length of Words
		port(
		-- Global Signals
		rst          : in  std_logic;                                               -- Global signals - Asynchronous reset
		clr          : in  std_logic;                                               -- Global signals - synchronous reset
		clk          : in  std_logic;                                               -- Global signals - clock, positive edge trigger
		en           : in  std_logic;                                               -- Global signals - Enable global signal
		--Input operands
		ope_en       : in  std_logic;                                               -- Operand - Enable
		ope_dividend : in  std_logic_vector(C_WORD_WIDTH-1 downto 0);               -- Operand - Dividend
		ope_divisor  : in  std_logic_vector(C_WORD_WIDTH-1 downto 0);               -- Operand - Divisor
		--Outpout results
		res_en       : out std_logic;                                               -- Result Enable 
		res_quotient : out std_logic_vector(C_WORD_WIDTH-1 downto 0);               -- Result Quotient
		res_remainder: out std_logic_vector(C_WORD_WIDTH-1 downto 0));              -- Result remainder
end division;

architecture rtl of division is

	------------------------------------------------------------------------------
	-- SIGNALS DECLARATION
	------------------------------------------------------------------------------
	signal idx_shft : integer range 0 to C_WORD_WIDTH;                            -- Index of Shift performed
	signal res_win  : std_logic;                                                  -- Result window
	signal a_reg    : std_logic_vector(C_WORD_WIDTH-1 downto 0);                  -- A register
	signal b_reg    : std_logic_vector(C_WORD_WIDTH-1 downto 0);                  -- B register
	signal p_reg    : std_logic_vector(C_WORD_WIDTH-1 downto 0);                  -- P register
	signal sq_reg   : std_logic;                                                  -- Sign Register for quotient  (only used with in signed mode)
	signal sr_reg   : std_logic;                                                  -- Sign Register for remainder (only used with in signed mode)

	-- Add user logic here if needed
	type FSM_State_type is (LOAD, DIVIDE, RESULT_ISSUE);
	signal State_reg : FSM_State_type := LOAD;
	
	signal p_shifted    : std_logic_vector(C_WORD_WIDTH-1 downto 0);                  -- P register
	signal cnt_reg      : unsigned(C_WORD_WIDTH-1 downto 0);                  -- P register
	signal Sub_reg      : signed(C_WORD_WIDTH-1 downto 0);
	
	signal a_reg_good    : std_logic_vector(C_WORD_WIDTH-1 downto 0);                  -- A register
	signal p_reg_good    : std_logic_vector(C_WORD_WIDTH-1 downto 0);                  -- P register
	signal ope_divisor_good  : std_logic_vector(C_WORD_WIDTH-1 downto 0);
	signal ope_dividend_good : std_logic_vector(C_WORD_WIDTH-1 downto 0);
	
begin  -- rtl

	----------------------vhdl_te--------------------------------------------------------
	-- The aim of this process is to perform the signed or unsigned division
	-- Report to details description for further information
	------------------------------------------------------------------------------
	proc_division:
	process(rst, clk)
	begin
		if rst = '1' then
			a_reg     <= (others=>'0');
			b_reg     <= (others=>'0');
			p_reg     <= (others=>'0');
			cnt_reg   <= to_unsigned(C_WORD_WIDTH-1, C_WORD_WIDTH);
			State_reg <= LOAD;
			sq_reg    <= '0'; 
			sr_reg    <= '0'; 
			res_remainder <= (others=>'0');
			res_quotient  <= (others=>'0');

		elsif rising_edge(clk) then
			case State_reg is 
				---------------------------------------------
				when LOAD => 
					if en='1' then
						if ope_en='1' then
							cnt_reg   <= to_unsigned(C_WORD_WIDTH-1, C_WORD_WIDTH);
--							a_reg     <= ope_dividend;
							b_reg     <= ope_divisor_good;
--							p_reg     <= (others=>'0');
							State_reg <= DIVIDE;
							
							p_reg(p_reg'length-2 downto 1) <= (others=>'0');
							p_reg(0) <= ope_dividend_good(a_reg'length-1);
							a_reg(a_reg'length-1 downto 1) <= ope_dividend_good(a_reg'length-2 downto 0);
							
							sq_reg    <= ope_dividend(ope_dividend'high) xor ope_divisor(ope_divisor'high); 
							sr_reg    <= ope_dividend(ope_dividend'high); 
						end if;
					end if;
				---------------------------------------------
				when DIVIDE => 
					if cnt_reg = 0 then
						State_reg     <= RESULT_ISSUE;
						res_remainder <= p_reg_good; 
						res_quotient  <= a_reg_good;
					else
						a_reg(a_reg'length-1 downto 1) <= a_reg(a_reg'length-2 downto 0);

						if Sub_reg<0 then 
							a_reg(0) <= '0';--set the low-order bit of A to 0 
							p_reg    <= p_shifted;--restore the old value of P 
						else
							a_reg(0) <= '1';-- otherwise to 1
							p_reg    <= STD_LOGIC_VECTOR(Sub_reg); -- otherwise store the result of subsract
						end if;
						cnt_reg <= cnt_reg-1;
					end if;
				---------------------------------------------
				when RESULT_ISSUE => 
					State_reg <= LOAD;
				---------------------------------------------
				when others => null;
			end case;
		end if;
	end process;
	
	Sub_reg   <= signed(p_shifted) - signed(b_reg);
	res_en    <= '1' when State_reg=RESULT_ISSUE else '0';
	p_shifted <= p_reg(p_reg'length-2 downto 0) & a_reg(a_reg'length-1);
	
	SignedModeConnect : if C_SIGNED_MODE=True generate
		ope_divisor_good  <= ope_divisor when ope_divisor(ope_divisor'high)='0' else STD_LOGIC_VECTOR(-signed(ope_divisor));
		ope_dividend_good <= ope_dividend when ope_dividend(ope_dividend'high)='0' else STD_LOGIC_VECTOR(-signed(ope_dividend));
		p_reg_good <= p_reg when sr_reg='0' else STD_LOGIC_VECTOR(-signed(p_reg));
		a_reg_good <= a_reg when sq_reg='0' else STD_LOGIC_VECTOR(-signed(a_reg));
	end generate;
	
	UnsignedModeConnect : if C_SIGNED_MODE=False generate
		ope_divisor_good  <= ope_divisor;
		ope_dividend_good <= ope_dividend;
		p_reg_good <= p_reg;
		a_reg_good <= a_reg;
	end generate;
	
	

end rtl;

