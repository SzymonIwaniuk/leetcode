defmodule Solution do
  @spec count_negatives(grid :: [[integer]]) :: integer
  def count_negatives(grid) do
    {n, m} = {length(grid), length(hd(grid))}
    count(grid, n - 1, 0, 0, m)
  end
  defp count(_grid, -1, _c, res, _m) do res end
  defp count(grid, r, c, res, m) when c >= m do
    count(grid, r - 1, c, res, m)
  end
  defp count(grid, r, c, res, m) do
    row = Enum.at(grid, r)
    num = Enum.at(row, c)

    if num >= 0 do
      count(grid, r, c + 1, res, m)
    else
      count(grid, r - 1, c, res + m - c, m)
    end
  end
end
