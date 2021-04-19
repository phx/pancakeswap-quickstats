# pancakeswap-quickstats

This is a script that I wrote over the course of a weekend which will return PancakeSwap stats from the command line.

I'm thinking about tweaking a local version of it to use BetterTouchTool in order to display some stats on my Macbook's Touch Bar.

After searching high and low for something like this, I was never satisfied with my results.

If you want results in the browser, [yieldwatch.net](https://yieldwatch.net) is probably the best resource.

There is even a Telegram bot that gives lots of useful information, ~~but the developer is kind of a dick~~.

Not to be confused with the Telegram bot referenced above, this originally started out as refactoring of the code from
[PancakeSwapInfo_bot](https://github.com/Ghonghito/PancakeSwapInfo_bot), but instead of forking it, I just made this its own project
since very little of the source code remained the same after I was finished.

That being said, [PancakeSwapInfo_bot](https://github.com/Ghonghito/PancakeSwapInfo_bot) is still a good resource if you are looking to
gain insight into multiple syrup pools and aren't worried about farm info.  You just may have to do a little translation, because a lot
of the code content is not in English.

Currently, this script only supports the CAKE syrup pool and the DFT/BNB farm info, but feel free to tweak as necessary to grab all of your relevant info.

## Installation and Usage

Replace the value of `wallet_addr` with your actual wallet address.

```
git clone https://github.com/phx/pancakeswap-quickstats
cd pancakeswap-quickstats
pip install -r requirements.txt
python3 cake.py
```

## Example Output

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

## Contributing

Feel free to fork the repo and submit a PR, and I will merge it as soon as I get around to it.

This is all under the MIT License, so feel free to do whatever you want with it and use it however you see fit.

Change it up, redistribute it as your own, I don't care.

I just wanted to share my knowledge with the community.
