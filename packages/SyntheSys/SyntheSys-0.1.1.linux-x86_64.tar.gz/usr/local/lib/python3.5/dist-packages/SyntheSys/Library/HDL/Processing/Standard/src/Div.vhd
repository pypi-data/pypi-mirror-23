
library IEEE;
use IEEE.std_logic_1164.all;
USE ieee.numeric_std.ALL;


entity Div is
	generic(
		DataWidth : natural := 64);
	port (
		Clk           : in  std_logic;
		Rst           : in  std_logic;
		A             : in  std_logic_vector(DataWidth-1 downto 0);
		B             : in  std_logic_vector(DataWidth-1 downto 0);
		R             : out std_logic_vector(DataWidth-1 downto 0);
		
		Start             : in  std_logic;
		DataRead          : out std_logic);

end Div;

architecture RTL of Div is

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
	
	ope_dividend <= A;
	ope_divisor  <= B;
	------------------------------------------------------------
	-- Configuration modes
	NetworkAdapter: entity work.NetworkAdapter(RTL)
		generic map(
			C_SIGNED_MODE => false,
			C_WORD_WIDTH  => DataWidth)
		port map(
			rst                => Rst,
			clk                => Clk,
			
			clr                => '0',
			en                 => en,
			ope_en             => ope_en,
			ope_dividend       => ope_dividend,
			ope_divisor        => ope_divisor,
			
			res_en             => res_en,
			res_quotient       => res_quotient,
			res_remainder      => res_remainder
			);

	R <= res_quotient;


end Div;


