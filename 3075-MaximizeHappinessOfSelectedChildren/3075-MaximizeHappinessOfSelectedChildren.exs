defmodule Solution do
  @spec maximum_happiness_sum(happiness :: [integer], k :: integer) :: integer
  def maximum_happiness_sum(happiness, k) do
    sorted = Enum.sort(happiness, &(&1 >= &2))
    rec(sorted, k, 0, 0)
  end 
  defp rec(list, 0, acc, d) do acc end
  defp rec([head | tail], k, acc, d) do
    cond do
      head - d > 0 -> rec(tail, k - 1, acc + head - d, d + 1)
      true -> acc
    end

      
