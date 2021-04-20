#!/usr/bin/env python3

import json, requests, sys

wallet_addr = '0xYOUR_WALLET_ADDRESS_HERE'

big = '============================================================'
div = '------------------------------------------------------------'

url = f"https://www.yieldwatch.net:443/api/all/{wallet_addr}?platforms=pancake"
headers = {"Connection": "close", "sec-ch-ua": "\"Chromium\";v=\"92\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"92\"", "Accept": "application/json, text/plain, */*", "DNT": "1", "Authorization": "Bearer undefined", "sec-ch-ua-mobile": "?0", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4475.0 Safari/537.36", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Dest": "empty", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9"}

def result_ok() -> bool:
    if status == "1":
        if message == "OK":
            return True
    return False

try:
    resp = requests.get(url, headers=headers).text
    data = json.loads(resp)
    status = data['status']
    message = data['message']
    result = data['result']
    if not result_ok:
        sys.exit(1)
except:
    sys.exit(1)

total_harvested = []
total_pending = []
pcs = data['result']['PancakeSwap']
total_usd_values = pcs['LPStaking']['totalUSDValues']
lp_staking_deposited = round(total_usd_values['deposit'], 2)
lp_staking_yield = round(total_usd_values['yield'], 2)
lp_staking_total = round(total_usd_values['total'], 2)
print(big)
print('LP Farms Staking:')
print(f'deposited: ${lp_staking_deposited:.2f}')
print(f'yield: ${lp_staking_yield:.2f}')
print(f'total: ${lp_staking_total:.2f}')
for v in pcs['LPStaking']['vaults']:
    print(div)
    v_type = v['type']
    v_name = v['name']
    v_platform = v['platform']
    v_reward_token = v['rewardToken']
    v_pending_rewards = round(float(v['pendingRewards']), 3)
    v_harvested_rewards = round(v['harvestedRewards'], 3)
    v_total_rewards = round(v['totalRewards'], 3)
    v_price_in_usd_reward_token = round(v['priceInUSDRewardToken'], 2)
    v_total_pending_usd = round(v_pending_rewards * v_price_in_usd_reward_token, 2)
    total_pending.append(v_total_pending_usd)
    v_total_harvested_usd = round(v_harvested_rewards * v_price_in_usd_reward_token, 2)
    total_harvested.append(v_total_harvested_usd)
    print(f'name: {v_name}')
    print(f'current price: ${v_price_in_usd_reward_token}')
    print(f'harvested: {v_harvested_rewards} {v_reward_token} (${v_total_harvested_usd:.2f})')
    print(f'pending rewards: {v_pending_rewards} {v_reward_token} (${round(v_pending_rewards * v_price_in_usd_reward_token, 2):.2f})')
    print(f'total rewards: {v_total_rewards} {v_reward_token} (${round(v_total_rewards * v_price_in_usd_reward_token, 2):.2f})')
print(big)
print('Syrup Pool Staking:')
syrup_staking_total_usd_values = pcs['staking']['totalUSDValues']
syrup_staking_deposited = round(syrup_staking_total_usd_values['deposit'], 2)
syrup_staking_yield = round(syrup_staking_total_usd_values['yield'], 2)
syrup_staking_total = round(syrup_staking_total_usd_values['total'], 2)
print(f'deposited: ${syrup_staking_deposited:.2f}')
print(f'yield: ${syrup_staking_yield:.2f}')
print(f'total: ${syrup_staking_total:.2f}')
for v in pcs['staking']['vaults']:
    print(div)
    v_type = v['type']
    v_name = v['name']
    v_platform = v['platform']
    v_deposit_token = v['depositToken']
    v_reward_token = v['rewardToken']
    v_deposited_tokens = round(v['depositedTokens'], 3)
    v_pending_rewards = round(float(v['pendingRewards']), 3)
    v_harvested_rewards = round(v['harvestedRewards'], 3)
    v_total_rewards = round(v['totalRewards'], 3)
    v_price_in_usd_reward_token = round(v['priceInUSDRewardToken'], 2)
    v_price_in_usd_deposit_token = round(v['priceInUSDDepositToken'], 2)
    v_total_pending_usd = round(v_pending_rewards * v_price_in_usd_reward_token, 2)
    total_pending.append(v_total_pending_usd)
    v_total_harvested_usd = round(v_harvested_rewards * v_price_in_usd_reward_token, 2)
    total_harvested.append(v_total_harvested_usd)
    print(f'name: {v_name}')
    print(f'current price: ${v_price_in_usd_reward_token}')
    print(f'deposited tokens: {v_deposited_tokens} {v_deposit_token} (${round(v_deposited_tokens * v_price_in_usd_deposit_token, 2):.2f})')
    print(f'harvested: {v_harvested_rewards} {v_reward_token} (${v_total_harvested_usd})')
    print(f'pending rewards: {v_pending_rewards} {v_reward_token} (${v_total_pending_usd:.2f})')
    print(f'total rewards: {v_total_rewards} {v_reward_token} (${round(v_total_rewards * v_price_in_usd_reward_token, 2):.2f})')
print(big)
sum_total_pending = round(sum(total_pending), 2)
sum_total_harvested = round(sum(total_harvested), 2)
sum_total_deposited = round(lp_staking_deposited + syrup_staking_deposited, 2)
sum_total_yield = round(sum_total_harvested + sum_total_pending, 2)
break_even = round(sum_total_deposited - sum_total_yield, 2)
print(f'total deposited: ${sum_total_deposited:.2f}')
print(f'total harvested: ${sum_total_harvested:.2f}')
print(f'total yield: ${sum_total_yield:.2f}')
if float(break_even) > 0:
    if not float(break_even) == 0:
        print(f'break even: ${break_even:.2f}')
print(f'pending rewards: ${sum_total_pending:.2f}')
print(big)
wallet_balance = data['result']['walletBalance']['totalUSDValue']
print(f'current wallet balance: ${round(wallet_balance, 2):.2f}')
print(big)

