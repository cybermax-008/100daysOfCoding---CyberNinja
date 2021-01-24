# We can write the length converter by using function clauses.

defmodule MeterToLengthConv do
    def convert(:feet,m) do
        m* 3.28084
    end

    def convert(:inch,m) do
        m* 39.3701
    end
end

