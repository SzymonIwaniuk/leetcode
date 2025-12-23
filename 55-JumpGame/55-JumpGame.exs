defmodule Solution do
  @spec can_jump(nums :: [integer]) :: boolean
  def can_jump(nums), do: do_can_jump(nums, 0)

  defp do_can_jump([], _reach), do: true

  defp do_can_jump([n | rest], reach) do
    cond do
      reach < 0 ->
        false

      true ->
        new_reach = max(reach, n) - 1
        do_can_jump(rest, new_reach)
    end
  end
end
