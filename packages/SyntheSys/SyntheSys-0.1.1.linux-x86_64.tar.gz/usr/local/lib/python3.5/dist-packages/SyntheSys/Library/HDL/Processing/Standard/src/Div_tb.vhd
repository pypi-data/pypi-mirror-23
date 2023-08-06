
library ieee;
use ieee.std_logic_1164.all;
use ieee.numeric_std.all;

library work;
use work.all;

entity Div_tb is
	generic (
		C_SIGNED_MODE : boolean := false;                                            -- Signed Mode configuration of division module
		C_WORD_WIDTH  : integer := 16);                                             -- Length of Words
end Div_tb;

architecture bench of Div_tb is


	-- Main component declaration
	
	component division is
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
			res_remainder: out std_logic_vector(C_WORD_WIDTH-1 downto 0));
	end component;

	

	signal clk : std_logic := '0';

	-- Signals to connect the instantiated multi-match component
	signal rst           : std_logic := '0';
	signal DataRead            : std_logic := '1';
	signal Start            : std_logic := '1';
	
	signal en           : std_logic;                                               -- Global signals - Enable global signal
	--Input operands
	signal ope_en       : std_logic;                                               -- Operand - Enable
	signal ope_dividend : std_logic_vector(C_WORD_WIDTH-1 downto 0);               -- Operand - Dividend
	signal ope_divisor  : std_logic_vector(C_WORD_WIDTH-1 downto 0);               -- Operand - Divisor
	--Outpout results
	signal res_en       : std_logic;                                               -- Result Enable 
	signal res_quotient : std_logic_vector(C_WORD_WIDTH-1 downto 0);               -- Result Quotient
	signal res_remainder: std_logic_vector(C_WORD_WIDTH-1 downto 0);
		

begin

	-- Clock generation
	Clk <= not Clk after 5 ns;

	Div : division 
		generic map(
			C_SIGNED_MODE => true,
			C_WORD_WIDTH  => 16)
		port map (
			rst                => Rst,
			clk                => Clk,
			clr                => '0',
			en                 => en,
			ope_en             => ope_en,
			ope_dividend       => ope_dividend,
			ope_divisor        => ope_divisor,
			
			res_en             => res_en,
			res_quotient       => res_quotient,
			res_remainder      => res_remainder);
	
	-- Process that generates stimuli
	process
	begin

		en     <= '1';
		rst    <= '1';
		ope_en <= '0';

		wait until rising_edge(clk);
		wait until rising_edge(clk);
		wait until rising_edge(clk);
		--wait for 200ns;
		--wait until rising_edge(clk);
		rst <= '0';
		wait until rising_edge(clk);
		ope_dividend <= X"000D";   -- => 13
		ope_divisor  <= X"0003";   -- => 3
		wait until rising_edge(clk);
		ope_en <= '1';
		wait until rising_edge(clk);
		ope_en <= '0';

		-- End of simulation
		wait for 200 ns;
		ope_dividend <= X"000D";   -- => 13
		ope_divisor  <= X"FFFD";   -- => -3
		wait until rising_edge(clk);
		ope_en <= '1';
		wait until rising_edge(clk);
		ope_en <= '0';

		-- End of simulation
		wait for 200 ns;
		ope_dividend <= X"FFF3";   -- => -13
		ope_divisor  <= X"0003";   -- => 3
		wait until rising_edge(clk);
		ope_en <= '1';
		wait until rising_edge(clk);
		ope_en <= '0';

		-- End of simulation
		wait for 200 ns;
		ope_dividend <= X"FFF3";   -- => -13
		ope_divisor  <= X"FFFD";   -- => 3
		wait until rising_edge(clk);
		ope_en <= '1';
		wait until rising_edge(clk);
		ope_en <= '0';

		-- End of simulation
		wait for 200 ns;
		
		assert false report "*** Test complete ***";
		wait;

	end process;



end architecture;


