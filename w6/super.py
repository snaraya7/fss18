# #Work in progress
#
# function super(data,goal,enough,       rows,most)
#   rows   = data.rows
#   goal   = goal or #(rows[1])
#   enough = enough or (#rows)^Lean.super.enough
#
#
#
# local function band(c,lo,hi)
#     if lo==1 then
#       return "..".. rows[hi][c]
#     elseif hi == most then
#       return rows[lo][c]..".."
#     else
#       return rows[lo][c]..".."..rows[hi][c] end
#   end
#
# local function argmin(c,lo,hi,
#                           x,xl,xr,bestx,tmpx,
#                           y,yl,yr,besty,tmpy,
#                           cut,mu)
#     xl,xr = num(), num()
#     yl,yr = num(), num()
#     for i=lo,hi do
#       numInc(xr, rows[i][c])
#       numInc(yr, rows[i][goal]) end
#     bestx = xr.sd
#     besty = yr.sd
#     mu    = yr.mu
#     if (hi - lo > 2*enough) then
#       for i=lo,hi do
#         x = rows[i][c]
#         y = rows[i][goal]
#         numInc(xl, x); numDec(xr, x)
#         numInc(yl, y); numDec(yr, y)
#         if xl.n >= enough and xr.n >= enough then
#           tmpx = numXpect(xl,xr) * Lean.super.margin
#           tmpy = numXpect(yl,yr) * Lean.super.margin
#           if tmpx < bestx then
#             if tmpy < besty then
#               cut,bestx,besty = i, tmpx, tmpy
#       end end end end end
#     return cut,mu
#   end
#
# local
# function
# cuts(c, lo, hi, pre, cut, txt, s, mu)
# txt = pre..rows[lo][c]..
# ".."..rows[hi][c]
# cut, mu = argmin(c, lo, hi)
# if cut then
# fyi(txt)
# cuts(c, lo, cut, pre..
# "|.. ")
# cuts(c, cut + 1, hi, pre..
# "|.. ")
# else
# s = band(c, lo, hi)
# fyi(txt..
# " ==> "..math.floor(100 * mu))
# for r=lo, hi do
# rows[r][c] = s
# end
# end
# end
#
#
# function stop(c,t)
#     for i=#t,1,-1 do if t[i][c] ~= "?" then return i end end
#     return 0
#   end
#
#  for _,c  in pairs(data.indeps) do
#     if data.nums[c] then
#       ksort(c,rows) -- sorts the rows on column `c`.
#       most = stop(c,rows)
#       fyi("\n-- ".. data.name[c] .. " ----------")
#       cuts(c,1,most,"|.. ") end end
#   print(gsub( cat(data.name,", "),
#               "%$","")) -- dump dollars since no more nums
#   dump(rows)
# end


