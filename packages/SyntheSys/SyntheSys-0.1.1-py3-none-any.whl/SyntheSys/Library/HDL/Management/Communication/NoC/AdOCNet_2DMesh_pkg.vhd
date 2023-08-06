
library IEEE;
use IEEE.std_logic_1164.all;

package AdOCNet_2DMesh_pkg is

	constant FlitWidth : natural := 16;
	constant DimX      : natural := 2;
	constant DimY      : natural := 2;
--	type FLITWIDTH_LOGIC is array(natural range <>) of std_logic_vector(FlitWidth-1 downto 0);
	type FLITS           is array(natural range <>) of std_logic_vector(FlitWidth-1 downto 0);
	type NATURALS        is array(natural range <>) of natural;
	type DIMX_x_DIMY_NUMERIC is array(natural range 0 to DimX*DimY-1) of natural;

end AdOCNet_2DMesh_pkg;

