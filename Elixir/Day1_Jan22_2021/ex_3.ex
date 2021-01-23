# Flattening the module hierarchy

defmodule MeterToLengthConv.Feet do
    def convert(m) do
        m*3.28084
    end
end

defmodule MeterToLengthConv.Inch do
    def convert(m) do
        m*39.3701
    end
end
