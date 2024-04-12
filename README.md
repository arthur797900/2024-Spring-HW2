# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1

Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward
(your tokenB balance).

> Solution
start amount:  5
5.666666666666667
2.467741935483871
5.117056856187291
20.205429200293473
Arbitrage opportunity: path: tokenB->tokenA->tokenD->tokenC->tokenB, tokenB balance=20.205429200293473

## Problem 2

What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution

在自動化做市商（AMM）系統中，滑點是指交易的預期價格與實際執行價格之間的差異。這種情況往往是由於在AMM中，價格是根據流動性池中兩種代幣的比例來決定的。當一筆交易執行時，它改變了這種比例，從而改變了價格。對於與池子大小相比較大的交易，這可能會導致顯著的價格變化，也就是滑點。

Uniswap V2通過允許用戶為他們的交易設定一個最大可接受的滑點來解決這個問題。當用戶發起交換時，他們可以設定一個交易的deadline（截止時間）和一個他們預期接收代幣的minimum amount（最小數量）。如果由於滑點導致實際收到的數量低於這個最小值，那麼交易將會失敗並回滾，從而保護用戶免受過度滑點的影響。

以下是一個文字描述的範例函數，說明Uniswap如何實現這一機制：

想像一個叫做swapExactTokensForTokens的函數，它允許用戶用確定數量的輸入代幣（amountIn）去交換他們期望的最小輸出代幣數量（amountOutMin）。用戶在調用這個函數時會設置一個截止時間（deadline），表示這筆交易最遲應該何時完成。

函數內部，它會先計算出基於當前流動性池狀態下的輸出代幣數量。如果這個數量低於用戶設定的amountOutMin，交易將不會執行。這樣，如果因為市場變化或者是大筆交易導致的價格滑動，用戶可以避免接受比他們預期更少的輸出代幣。

在Uniswap V2中，函數可能會檢查流動性池中的代幣餘額，確定用戶可以交換的數量，並在這個過程中使用了一些安全檢查（如確保交易不會在截止時間後執行）。如果這些檢查不通過，交易將回滾，並且用戶支付的輸入代幣將返回給用戶，從而保護他們免受不利的價格變動。

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution

在UniswapV2Pair合約中的鑄造（mint）函數用於當添加流動性時創建新的流動性代幣。根據Uniswap V2的協定，在首次鑄造流動性代幣時，會從使用者的初始存款中扣除一個最小數量的流動性，這樣做是為了在合約中創建永久鎖定的流動性，以確保合約永遠有一定數量的流動性，這有助於預防某些潛在的金融攻擊，增強合約的安全性。

具體而言，當第一個流動性提供者向合約存入代幣時，他們為該流動性池注入了新的流動性，而這個最小流動性數額的扣除可視作該池的「創始份額」。在Uniswap V2中，這個數量被設定為最小流動性代幣數MINIMUM_LIQUIDITY（例如1000流動性代幣）。這樣設計的目的是為了確保在流動性價格非常低的情況下，不會因為四捨五入的誤差而導致代幣價值扭曲。

這個最小流動性並不會被分配給任何人，而是被永久地鎖定在合約中。這預防了第一個流動性提供者立刻取回所有流動性，導致代幣價格歸零的情況。這個機制也提升了早期流動性提供者的進入門檻，從而在一定程度上防範了惡意的經濟行為，增加了對於早期提供者的責任和承諾。同時，這樣的設計還確保了合約內部計算和流動性交換的完整性，預防了可能的整數溢出錯誤。

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution

在Uniswap V2合約的鑄造函數中，非首次存入代幣時，利用特定公式計算流動性，目的是保證流動性提供者按照他們提供的代幣比例獲得流動性代幣。這樣確保流動性提供者能夠公平地分配交易費用，並防止後來者稀釋早期流動性提供者的份額。這促進了流動性的長期穩定，維持了交易的公平性和協議的效率。
## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution

夾子攻擊是一種在去中心化金融（DeFi）空間中常見的惡意交易策略，攻擊者會在用戶發起交換（swap）之前和之後，故意進行兩筆交易。當攻擊者察覺到一個大筆交易即將執行時，他們會先以較高價格執行一筆小交易，推高價格，然後用戶的大交易隨後執行，因價格提高而付出更多，最後攻擊者再以更低的價格完成另一筆交易，從而從中獲利。

當你發起交換時，如果成為夾子攻擊的目標，可能會導致你獲得的代幣數量少於預期，因為你的交易被攻擊者用來推高或拉低市場價格。這會導致你為同樣數量的輸入代幣支付更多，或者為輸入的代幣獲得更少的輸出代幣，增加了交易成本和滑點。