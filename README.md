# pancakeswap-quickstats

This is a set of scripts that I wrote over the course of a weekend which will return PancakeSwap stats from the command line.

I was thinking about tweaking a local version of it to use BetterTouchTool in order to display some stats on my Macbook's Touch Bar,
but I ended up writing a small shell script plugin for [xbar](https://github.com/matryer/xbar) that parses the output of [`watch.py`](./watch.py)
and displays the output in my menu bar like `CAKE [POOL YIELD] [FARM YIELD] [TOTAL PENDING USD]`.

After searching high and low for a PancakeSwap command line tool, I was never satisfied with the results, so these two scripts are what I came up with.

## cake.py

I was looking for resources, and [`cake.py`](./cake.py) was the first script that I created. It interacts directly with smart contracts on the
Binance Smart Chain and relies on the Coingecko API via a built-in python module.  Some of the code was appropriated from another project I found,
details below:

I found a Telegram bot that gives most of the relevant info I was looking for, but the developer ~~was  kind of a dick~~ didn't want to share any
tips on how to generate that info, and the bot was closed source because it is monetized.

Not to be confused with the Telegram bot referenced above, this originally started out as refactoring of the code from
[PancakeSwapInfo_bot](https://github.com/Ghonghito/PancakeSwapInfo_bot), but instead of forking it, I just made this its own project
since very little of the source code remained the same after I was finished.

That being said, [PancakeSwapInfo_bot](https://github.com/Ghonghito/PancakeSwapInfo_bot) is still a good resource if you are looking to
gain insight into multiple syrup pools and aren't worried about farm info.  You just may have to do a little translation, because a lot
of the code content is not in English.

Currently, this script only supports the CAKE syrup pool and the DFT/BNB farm info, but feel free to tweak as necessary to grab all of your relevant info.

## watch.py

This is a script that only relies on the yieldwatch API.  It's not as trusty as [`cake.py`](./cake.py) because of its reliance on the yieldwatch API,
however, it does offer a bit more informative data, and this one is scripted in a way that I think it should be able to work with multiple farms
and pools straight out of the gate, but feel free to customize as necessary.

That being said, if you are just looking for results in the browser, [yieldwatch.net](https://yieldwatch.net) is probably the best resource.


## Installation and Usage

Replace the value of `wallet_addr` with your actual wallet address.

```
git clone https://github.com/phx/pancakeswap-quickstats
cd pancakeswap-quickstats
pip install -r requirements.txt
python3 cake.py
[OR]
python3 watch.py
```

## Example Output for cake.py

```
====================================================
🥞 CURRENT CAKE PRICE: $22.19
====================================================
DFT-BNB FARM:
----------------------------------------------------
🔹 staked lp tokens: 8.552
💵 pending cake rewards: 0.859 ($19.07)
====================================================
SYRUP POOL:
----------------------------------------------------
🔹 staked cake: 3.775 ($83.77)
💵 pending cake rewards: 0.073 ($1.62)
====================================================
🥞 READY TO HARVEST: 0.932 CAKE ($20.69)
====================================================
```

## Example Output for watch.py

```
============================================================
LP Farms Staking:
deposited: $303.04
yield: $23.24
total: $326.27
------------------------------------------------------------
name: DFT-WBNB Pool
current price: $23.87
harvested: 1.422 CAKE ($33.94)
pending rewards: 0.973 CAKE ($23.23)
total rewards: 2.395 CAKE ($57.17)
============================================================
Syrup Pool Staking:
deposited: $90.11
yield: $1.98
total: $92.09
------------------------------------------------------------
name: Cake-Cake Staking
current price: $23.87
deposited tokens: 3.775 Cake ($90.11)
harvested: 0.141 Cake ($3.37)
pending rewards: 0.083 Cake ($1.98)
total rewards: 0.224 Cake ($5.35)
============================================================
total deposited: $393.15
total harvested: $37.31
total yield: $62.52
break even: $330.63
pending rewards: $25.21
============================================================
current wallet balance: $27.98
============================================================
```

## Contributing

Feel free to fork the repo and submit a PR, and I will merge it as soon as I get around to it.

This is all under the MIT License, so feel free to do whatever you want with it and use it however you see fit.

Change it up, redistribute it as your own, I don't care.

I just wanted to share my knowledge with the community.
