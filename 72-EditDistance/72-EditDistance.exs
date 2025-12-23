defmodule Solution do
  @spec min_distance(word1 :: String.t, word2 :: String.t) :: integer
  def min_distance(word1, word2) do
    n = String.length(word1)
    m = String.length(word2)

    rec(0, 0, word1, word2, n, m, %{})
    |> elem(0)
  end

  defp rec(i, j, word1, word2, n, m, memo) do
    case Map.get(memo, {i, j}) do
      nil -> 
        cond do
          n == i and m == j -> 
            {0, memo}

          n > i and m == j ->
            {n - i, memo}

          m > j and n == i ->
            {m - j, memo}

          true ->
            {mini, memo_f} = 
              if String.at(word1, i) == String.at(word2, j) do
                {val, memo2} = rec(i + 1, j + 1, word1, word2, n, m, memo)
                {val, memo2}
              else
                {del, memo2} = rec(i + 1, j, word1, word2, n, m, memo)
                {rep, memo3} = rec(i + 1, j + 1, word1, word2, n, m, memo2)
                {ins, memo4} = rec(i, j + 1, word1, word2, n, m, memo3)
                mini_val = min(del + 1, min(rep + 1, ins + 1))
                {mini_val, memo4}
              end

            memo_f = Map.put(memo_f, {i, j}, mini)
            {mini, memo_f}
        end

      value -> 
        {value, memo}
    end
  end
end

