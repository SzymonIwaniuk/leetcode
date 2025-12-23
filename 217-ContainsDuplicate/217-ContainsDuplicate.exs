defmodule Solution do
  @spec contains_duplicate(nums :: [integer]) :: boolean
  def contains_duplicate(nums) do
    length(nums) != length(Enum.uniq(nums))
    
  end
end
