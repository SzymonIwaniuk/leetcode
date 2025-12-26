defmodule Solution do
  @spec best_closing_time(customers :: String.t) :: integer
  def best_closing_time(customers) do
    charlist = String.to_charlist(customers)
    tuple = Enum.reduce(
        charlist, 
        {0, 0 ,0 ,-1}, 
        fn ch, {score, max_score, i,  time} ->
        new_score = 
          if ch == ?Y do
            score + 1
          else
            score - 1
          end

        if new_score > max_score do
          {new_score, new_score, i + 1, i}
        else
          {new_score, max_score, i + 1, time}
        end
    end)
    elem(tuple, 3) + 1
  end
end
