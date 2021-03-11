from discord.ext import commands

import discord
import json
import os
from web3 import Web3
from cryptoaddress import EthereumAddress

client = discord.Client()
token = 'DISCORD_TOKEN'
bot = commands.Bot(command_prefix='!')

w3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/PUT_YOUR_API_KEY_HERE'))

wp_abi = '[{"inputs":[{"internalType":"contract SURF","name":"_surf","type":"address"},{"internalType":"contract Tito",' \
         '"name":"_tito","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,' \
         '"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":false,' \
         '"internalType":"uint256","name":"surfAmount","type":"uint256"}],"name":"Claim","type":"event"},' \
         '{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},' \
         '{"indexed":false,"internalType":"uint256","name":"ethReward","type":"uint256"}],"name":"EthRewardAdded",' \
         '"type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner",' \
         '"type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],' \
         '"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,' \
         '"internalType":"address","name":"user","type":"address"},{"indexed":false,"internalType":"uint256",' \
         '"name":"amount","type":"uint256"}],"name":"Stake","type":"event"},{"anonymous":false,"inputs":[{' \
         '"indexed":true,"internalType":"address","name":"user","type":"address"},{"indexed":false,' \
         '"internalType":"uint256","name":"surfReward","type":"uint256"}],"name":"SurfRewardAdded","type":"event"},' \
         '{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"user","type":"address"},' \
         '{"indexed":false,"internalType":"uint256","name":"amount","type":"uint256"}],"name":"Withdraw",' \
         '"type":"event"},{"inputs":[],"name":"INITIAL_PAYOUT_INTERVAL","outputs":[{"internalType":"uint256","name":"",' \
         '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"accSurfPerShare",' \
         '"outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},' \
         '{"inputs":[],"name":"activate","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],' \
         '"name":"active","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view",' \
         '"type":"function"},{"inputs":[],"name":"addEthReward","outputs":[],"stateMutability":"payable",' \
         '"type":"function"},{"inputs":[{"internalType":"address","name":"_from","type":"address"},' \
         '{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"addSurfReward","outputs":[],' \
         '"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"claim","outputs":[],' \
         '"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_user",' \
         '"type":"address"}],"name":"getAllInfoFor","outputs":[{"internalType":"bool","name":"isActive","type":"bool"},' \
         '{"internalType":"uint256[12]","name":"info","type":"uint256[12]"}],"stateMutability":"view",' \
         '"type":"function"},{"inputs":[],"name":"initialSurfReward","outputs":[{"internalType":"uint256","name":"",' \
         '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"initialSurfRewardPerDay",' \
         '"outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},' \
         '{"inputs":[],"name":"lastPayout","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],' \
         '"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address",' \
         '"name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"payoutNumber",' \
         '"outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},' \
         '{"inputs":[{"internalType":"address","name":"_tokenAddress","type":"address"}],"name":"recoverERC20",' \
         '"outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership",' \
         '"outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256",' \
         '"name":"_payoutNumber","type":"uint256"}],"name":"rewardAtPayout","outputs":[{"internalType":"uint256",' \
         '"name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256",' \
         '"name":"_unstakingFee","type":"uint256"},{"internalType":"uint256","name":"_convertToSurfAmount",' \
         '"type":"uint256"}],"name":"setUnstakingFee","outputs":[],"stateMutability":"nonpayable","type":"function"},' \
         '{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"stake","outputs":[],' \
         '"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"_user",' \
         '"type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"stakeFor","outputs":[' \
         '],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"startTime","outputs":[{' \
         '"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[' \
         '],"name":"surf","outputs":[{"internalType":"contract SURF","name":"","type":"address"}],' \
         '"stateMutability":"view","type":"function"},{"inputs":[],"name":"surfPool","outputs":[{' \
         '"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},' \
         '{"inputs":[],"name":"timeUntilNextPayout","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],' \
         '"stateMutability":"view","type":"function"},{"inputs":[],"name":"tito","outputs":[{"internalType":"contract ' \
         'Tito","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],' \
         '"name":"totalPendingSurf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],' \
         '"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalStaked","outputs":[{' \
         '"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{' \
         '"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],' \
         '"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"uniswapRouter","outputs":[{' \
         '"internalType":"contract IUniswapV2Router02","name":"","type":"address"}],"stateMutability":"view",' \
         '"type":"function"},{"inputs":[],"name":"unstakingFee","outputs":[{"internalType":"uint256","name":"",' \
         '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],' \
         '"name":"unstakingFeeConvertToSurfAmount","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],' \
         '"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],' \
         '"name":"userInfo","outputs":[{"internalType":"uint256","name":"staked","type":"uint256"},' \
         '{"internalType":"uint256","name":"rewardDebt","type":"uint256"},{"internalType":"uint256","name":"claimed",' \
         '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"weth","outputs":[{' \
         '"internalType":"contract IERC20","name":"","type":"address"}],"stateMutability":"view","type":"function"},' \
         '{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"}],"name":"withdraw","outputs":[],' \
         '"stateMutability":"nonpayable","type":"function"},{"stateMutability":"payable","type":"receive"}] '

board_abi = '[{"constant":true,"inputs":[{"name":"interfaceId","type":"bytes4"}],"name":"supportsInterface",' \
            '"outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},' \
            '{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,' \
            '"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"tokenId",' \
            '"type":"uint256"}],"name":"getApproved","outputs":[{"name":"","type":"address"}],"payable":false,' \
            '"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},' \
            '{"name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"payable":false,' \
            '"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"giver",' \
            '"type":"address"},{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],' \
            '"name":"batchTransfer","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},' \
            '{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],' \
            '"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"from",' \
            '"type":"address"},{"name":"to","type":"address"},{"name":"tokenId","type":"uint256"}],' \
            '"name":"transferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},' \
            '{"constant":true,"inputs":[{"name":"owner","type":"address"},{"name":"index","type":"uint256"}],' \
            '"name":"tokenOfOwnerByIndex","outputs":[{"name":"","type":"uint256"}],"payable":false,' \
            '"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"from",' \
            '"type":"address"},{"name":"to","type":"address"},{"name":"tokenId","type":"uint256"}],' \
            '"name":"safeTransferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable",' \
            '"type":"function"},{"constant":false,"inputs":[{"name":"tokenId","type":"uint256"}],"name":"burn",' \
            '"outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,' \
            '"inputs":[],"name":"destroyAndSend","outputs":[],"payable":false,"stateMutability":"nonpayable",' \
            '"type":"function"},{"constant":true,"inputs":[{"name":"index","type":"uint256"}],"name":"tokenByIndex",' \
            '"outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},' \
            '{"constant":true,"inputs":[],"name":"maker","outputs":[{"name":"","type":"address"}],"payable":false,' \
            '"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},' \
            '{"name":"tokenId","type":"uint256"},{"name":"tokenURI","type":"string"}],"name":"mintWithTokenURI",' \
            '"outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},' \
            '{"constant":true,"inputs":[{"name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"name":"",' \
            '"type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,' \
            '"inputs":[{"name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"",' \
            '"type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,' \
            '"inputs":[],"name":"renounceOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable",' \
            '"type":"function"},{"constant":false,"inputs":[{"name":"_tokenId","type":"uint256"}],"name":"buyThing",' \
            '"outputs":[{"name":"","type":"bool"}],"payable":true,"stateMutability":"payable","type":"function"},' \
            '{"constant":true,"inputs":[{"name":"owner","type":"address"}],"name":"tokensOfOwner","outputs":[{' \
            '"name":"","type":"uint256[]"}],"payable":false,"stateMutability":"view","type":"function"},' \
            '{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,' \
            '"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"isOwner","outputs":[{' \
            '"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,' \
            '"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,' \
            '"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"account",' \
            '"type":"address"}],"name":"addMinter","outputs":[],"payable":false,"stateMutability":"nonpayable",' \
            '"type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},{"name":"amountToMint",' \
            '"type":"uint256"},{"name":"metaId","type":"string"},{"name":"setPrice","type":"uint256"},' \
            '{"name":"isForSale","type":"bool"}],"name":"batchMint","outputs":[],"payable":false,' \
            '"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"renounceMinter",' \
            '"outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,' \
            '"inputs":[],"name":"baseUri","outputs":[{"name":"","type":"string"}],"payable":false,' \
            '"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},' \
            '{"name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"payable":false,' \
            '"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"account",' \
            '"type":"address"}],"name":"isMinter","outputs":[{"name":"","type":"bool"}],"payable":false,' \
            '"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"id","outputs":[{' \
            '"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},' \
            '{"constant":false,"inputs":[{"name":"from","type":"address"},{"name":"to","type":"address"},' \
            '{"name":"tokenId","type":"uint256"},{"name":"_data","type":"bytes"}],"name":"safeTransferFrom",' \
            '"outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,' \
            '"inputs":[{"name":"","type":"uint256"}],"name":"items","outputs":[{"name":"tokenId","type":"uint256"},' \
            '{"name":"price","type":"uint256"},{"name":"metaId","type":"string"},{"name":"state","type":"uint8"}],' \
            '"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{' \
            '"name":"_tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"name":"","type":"string"}],' \
            '"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"ids",' \
            '"type":"uint256[]"},{"name":"isEnabled","type":"bool"}],"name":"setTokenState","outputs":[],' \
            '"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{' \
            '"name":"tokenIds","type":"uint256[]"}],"name":"batchBurn","outputs":[],"payable":false,' \
            '"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"ids",' \
            '"type":"uint256[]"},{"name":"setPrice","type":"uint256"}],"name":"setTokenPrice","outputs":[],' \
            '"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{' \
            '"name":"owner","type":"address"},{"name":"operator","type":"address"}],"name":"isApprovedForAll",' \
            '"outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},' \
            '{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[' \
            '],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"name",' \
            '"type":"string"},{"name":"symbol","type":"string"},{"name":"uri","type":"string"},{"name":"fee",' \
            '"type":"address"},{"name":"creator","type":"address"}],"payable":false,"stateMutability":"nonpayable",' \
            '"type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"error","type":"string"},' \
            '{"indexed":false,"name":"tokenId","type":"uint256"}],"name":"ErrorOut","type":"event"},' \
            '{"anonymous":false,"inputs":[{"indexed":false,"name":"metaId","type":"string"},{"indexed":false,' \
            '"name":"recipients","type":"address[]"},{"indexed":false,"name":"ids","type":"uint256[]"}],' \
            '"name":"BatchTransfered","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"id",' \
            '"type":"uint256"},{"indexed":false,"name":"metaId","type":"string"}],"name":"Minted","type":"event"},' \
            '{"anonymous":false,"inputs":[{"indexed":false,"name":"metaId","type":"string"},{"indexed":false,' \
            '"name":"ids","type":"uint256[]"}],"name":"BatchBurned","type":"event"},{"anonymous":false,"inputs":[{' \
            '"indexed":false,"name":"ids","type":"uint256[]"},{"indexed":false,"name":"metaId","type":"string"}],' \
            '"name":"BatchForSale","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"tokenId",' \
            '"type":"uint256"},{"indexed":false,"name":"metaId","type":"string"},{"indexed":false,"name":"value",' \
            '"type":"uint256"}],"name":"Bought","type":"event"},{"anonymous":false,"inputs":[],"name":"Destroy",' \
            '"type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"previousOwner","type":"address"},' \
            '{"indexed":true,"name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},' \
            '{"anonymous":false,"inputs":[{"indexed":true,"name":"account","type":"address"}],"name":"MinterAdded",' \
            '"type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"account","type":"address"}],' \
            '"name":"MinterRemoved","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from",' \
            '"type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":true,"name":"tokenId",' \
            '"type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,' \
            '"name":"owner","type":"address"},{"indexed":true,"name":"approved","type":"address"},{"indexed":true,' \
            '"name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{' \
            '"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"operator","type":"address"},' \
            '{"indexed":false,"name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"}] '

surf_abi = '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},' \
           '{"indexed":true,"internalType":"address","name":"spender","type":"address"},{"indexed":false,' \
           '"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval","type":"event"},' \
           '{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"delegator",' \
           '"type":"address"},{"indexed":true,"internalType":"address","name":"fromDelegate","type":"address"},' \
           '{"indexed":true,"internalType":"address","name":"toDelegate","type":"address"}],"name":"DelegateChanged",' \
           '"type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"delegate",' \
           '"type":"address"},{"indexed":false,"internalType":"uint256","name":"previousBalance","type":"uint256"},' \
           '{"indexed":false,"internalType":"uint256","name":"newBalance","type":"uint256"}],' \
           '"name":"DelegateVotesChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,' \
           '"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,' \
           '"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred",' \
           '"type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from",' \
           '"type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},' \
           '{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Transfer",' \
           '"type":"event"},{"inputs":[],"name":"DELEGATION_TYPEHASH","outputs":[{"internalType":"bytes32","name":"",' \
           '"type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"DOMAIN_TYPEHASH",' \
           '"outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view",' \
           '"type":"function"},{"inputs":[],"name":"MAX_SUPPLY","outputs":[{"internalType":"uint256","name":"",' \
           '"type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bool",' \
           '"name":"_addToSenderWhitelist","type":"bool"},{"internalType":"address","name":"_address",' \
           '"type":"address"}],"name":"addToTransferWhitelist","outputs":[],"stateMutability":"nonpayable",' \
           '"type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},' \
           '{"internalType":"address","name":"spender","type":"address"}],"name":"allowance","outputs":[{' \
           '"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},' \
           '{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256",' \
           '"name":"amount","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"",' \
           '"type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address",' \
           '"name":"_spender","type":"address"},{"internalType":"uint256","name":"_tokens","type":"uint256"},' \
           '{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"approveAndCall","outputs":[{' \
           '"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},' \
           '{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{' \
           '"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},' \
           '{"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"uint32","name":"",' \
           '"type":"uint32"}],"name":"checkpoints","outputs":[{"internalType":"uint32","name":"fromBlock",' \
           '"type":"uint32"},{"internalType":"uint256","name":"votes","type":"uint256"}],"stateMutability":"view",' \
           '"type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"",' \
           '"type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address",' \
           '"name":"spender","type":"address"},{"internalType":"uint256","name":"subtractedValue","type":"uint256"}],' \
           '"name":"decreaseAllowance","outputs":[{"internalType":"bool","name":"","type":"bool"}],' \
           '"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address",' \
           '"name":"delegatee","type":"address"}],"name":"delegate","outputs":[],"stateMutability":"nonpayable",' \
           '"type":"function"},{"inputs":[{"internalType":"address","name":"delegatee","type":"address"},' \
           '{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"uint256","name":"expiry",' \
           '"type":"uint256"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32",' \
           '"name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],' \
           '"name":"delegateBySig","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{' \
           '"internalType":"address","name":"delegator","type":"address"}],"name":"delegates","outputs":[{' \
           '"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},' \
           '{"inputs":[{"internalType":"address","name":"account","type":"address"}],"name":"getCurrentVotes",' \
           '"outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view",' \
           '"type":"function"},{"inputs":[{"internalType":"address","name":"account","type":"address"},' \
           '{"internalType":"uint256","name":"blockNumber","type":"uint256"}],"name":"getPriorVotes","outputs":[{' \
           '"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},' \
           '{"inputs":[{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256",' \
           '"name":"addedValue","type":"uint256"}],"name":"increaseAllowance","outputs":[{"internalType":"bool",' \
           '"name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[],' \
           '"name":"maxSupplyHit","outputs":[{"internalType":"bool","name":"","type":"bool"}],' \
           '"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_to",' \
           '"type":"address"},{"internalType":"uint256","name":"_amount","type":"uint256"}],' \
           '"name":"migrateLockedLPTokens","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[' \
           '{"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_amount",' \
           '"type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"nonpayable","type":"function"},' \
           '{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],' \
           '"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"",' \
           '"type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],' \
           '"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"",' \
           '"type":"address"}],"name":"numCheckpoints","outputs":[{"internalType":"uint32","name":"",' \
           '"type":"uint32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{' \
           '"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},' \
           '{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"recipientWhitelist","outputs":[' \
           '{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{' \
           '"internalType":"bool","name":"_removeFromSenderWhitelist","type":"bool"},{"internalType":"address",' \
           '"name":"_address","type":"address"}],"name":"removeFromTransferWhitelist","outputs":[],' \
           '"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],' \
           '"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"",' \
           '"type":"address"}],"name":"senderWhitelist","outputs":[{"internalType":"bool","name":"","type":"bool"}],' \
           '"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_titoAddress",' \
           '"type":"address"},{"internalType":"address payable","name":"_whirlpoolAddress","type":"address"},' \
           '{"internalType":"address","name":"_surfPoolAddress","type":"address"}],"name":"setContractAddresses",' \
           '"outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256",' \
           '"name":"_transferFee","type":"uint256"}],"name":"setTransferFee","outputs":[],' \
           '"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"surfPoolAddress","outputs":[{' \
           '"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},' \
           '{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],' \
           '"stateMutability":"view","type":"function"},{"inputs":[],"name":"titoAddress","outputs":[{' \
           '"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},' \
           '{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],' \
           '"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"recipient",' \
           '"type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"transfer",' \
           '"outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable",' \
           '"type":"function"},{"inputs":[{"internalType":"address","name":"_to","type":"address"},' \
           '{"internalType":"uint256","name":"_tokens","type":"uint256"},{"internalType":"bytes","name":"_data",' \
           '"type":"bytes"}],"name":"transferAndCall","outputs":[{"internalType":"bool","name":"","type":"bool"}],' \
           '"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"transferFee","outputs":[{' \
           '"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},' \
           '{"inputs":[{"internalType":"address","name":"sender","type":"address"},{"internalType":"address",' \
           '"name":"recipient","type":"address"},{"internalType":"uint256","name":"amount","type":"uint256"}],' \
           '"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],' \
           '"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner",' \
           '"type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable",' \
           '"type":"function"},{"inputs":[],"name":"whirlpoolAddress","outputs":[{"internalType":"address payable",' \
           '"name":"","type":"address"}],"stateMutability":"view","type":"function"}] '

lev_abi = '[{"constant":true,"inputs":[{"name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[' \
          '{"name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,' \
          '"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,' \
          '"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"tokenId",' \
          '"type":"uint256"}],"name":"getApproved","outputs":[{"name":"","type":"address"}],"payable":false,' \
          '"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},' \
          '{"name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"payable":false,' \
          '"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"giver",' \
          '"type":"address"},{"name":"recipients","type":"address[]"},{"name":"values","type":"uint256[]"}],' \
          '"name":"batchTransfer","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},' \
          '{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],' \
          '"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"from",' \
          '"type":"address"},{"name":"to","type":"address"},{"name":"tokenId","type":"uint256"}],' \
          '"name":"transferFrom","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},' \
          '{"constant":true,"inputs":[{"name":"owner","type":"address"},{"name":"index","type":"uint256"}],' \
          '"name":"tokenOfOwnerByIndex","outputs":[{"name":"","type":"uint256"}],"payable":false,' \
          '"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"from","type":"address"},' \
          '{"name":"to","type":"address"},{"name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[' \
          '],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{' \
          '"name":"tokenId","type":"uint256"}],"name":"burn","outputs":[],"payable":false,' \
          '"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"destroyAndSend",' \
          '"outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,' \
          '"inputs":[{"name":"index","type":"uint256"}],"name":"tokenByIndex","outputs":[{"name":"",' \
          '"type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,' \
          '"inputs":[],"name":"maker","outputs":[{"name":"","type":"address"}],"payable":false,' \
          '"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},' \
          '{"name":"tokenId","type":"uint256"},{"name":"tokenURI","type":"string"}],"name":"mintWithTokenURI",' \
          '"outputs":[{"name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},' \
          '{"constant":true,"inputs":[{"name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"name":"",' \
          '"type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,' \
          '"inputs":[{"name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],' \
          '"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[],' \
          '"name":"renounceOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},' \
          '{"constant":false,"inputs":[{"name":"_tokenId","type":"uint256"}],"name":"buyThing","outputs":[{"name":"",' \
          '"type":"bool"}],"payable":true,"stateMutability":"payable","type":"function"},{"constant":true,"inputs":[{' \
          '"name":"owner","type":"address"}],"name":"tokensOfOwner","outputs":[{"name":"","type":"uint256[]"}],' \
          '"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"owner",' \
          '"outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},' \
          '{"constant":true,"inputs":[],"name":"isOwner","outputs":[{"name":"","type":"bool"}],"payable":false,' \
          '"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{' \
          '"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,' \
          '"inputs":[{"name":"account","type":"address"}],"name":"addMinter","outputs":[],"payable":false,' \
          '"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"to",' \
          '"type":"address"},{"name":"amountToMint","type":"uint256"},{"name":"metaId","type":"string"},' \
          '{"name":"setPrice","type":"uint256"},{"name":"isForSale","type":"bool"}],"name":"batchMint","outputs":[],' \
          '"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],' \
          '"name":"renounceMinter","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},' \
          '{"constant":true,"inputs":[],"name":"baseUri","outputs":[{"name":"","type":"string"}],"payable":false,' \
          '"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"to","type":"address"},' \
          '{"name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"payable":false,' \
          '"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"account",' \
          '"type":"address"}],"name":"isMinter","outputs":[{"name":"","type":"bool"}],"payable":false,' \
          '"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"id","outputs":[{' \
          '"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},' \
          '{"constant":false,"inputs":[{"name":"from","type":"address"},{"name":"to","type":"address"},' \
          '{"name":"tokenId","type":"uint256"},{"name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[' \
          '],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"name":"",' \
          '"type":"uint256"}],"name":"items","outputs":[{"name":"tokenId","type":"uint256"},{"name":"price",' \
          '"type":"uint256"},{"name":"metaId","type":"string"},{"name":"state","type":"uint8"}],"payable":false,' \
          '"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_tokenId",' \
          '"type":"uint256"}],"name":"tokenURI","outputs":[{"name":"","type":"string"}],"payable":false,' \
          '"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"ids","type":"uint256[]"},' \
          '{"name":"isEnabled","type":"bool"}],"name":"setTokenState","outputs":[],"payable":false,' \
          '"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"tokenIds",' \
          '"type":"uint256[]"}],"name":"batchBurn","outputs":[],"payable":false,"stateMutability":"nonpayable",' \
          '"type":"function"},{"constant":false,"inputs":[{"name":"ids","type":"uint256[]"},{"name":"setPrice",' \
          '"type":"uint256"}],"name":"setTokenPrice","outputs":[],"payable":false,"stateMutability":"nonpayable",' \
          '"type":"function"},{"constant":true,"inputs":[{"name":"owner","type":"address"},{"name":"operator",' \
          '"type":"address"}],"name":"isApprovedForAll","outputs":[{"name":"","type":"bool"}],"payable":false,' \
          '"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"newOwner",' \
          '"type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable",' \
          '"type":"function"},{"inputs":[{"name":"name","type":"string"},{"name":"symbol","type":"string"},' \
          '{"name":"uri","type":"string"},{"name":"fee","type":"address"},{"name":"creator","type":"address"}],' \
          '"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{' \
          '"indexed":false,"name":"error","type":"string"},{"indexed":false,"name":"tokenId","type":"uint256"}],' \
          '"name":"ErrorOut","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"metaId",' \
          '"type":"string"},{"indexed":false,"name":"recipients","type":"address[]"},{"indexed":false,"name":"ids",' \
          '"type":"uint256[]"}],"name":"BatchTransfered","type":"event"},{"anonymous":false,"inputs":[{' \
          '"indexed":false,"name":"id","type":"uint256"},{"indexed":false,"name":"metaId","type":"string"}],' \
          '"name":"Minted","type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"name":"metaId",' \
          '"type":"string"},{"indexed":false,"name":"ids","type":"uint256[]"}],"name":"BatchBurned","type":"event"},' \
          '{"anonymous":false,"inputs":[{"indexed":false,"name":"ids","type":"uint256[]"},{"indexed":false,' \
          '"name":"metaId","type":"string"}],"name":"BatchForSale","type":"event"},{"anonymous":false,"inputs":[{' \
          '"indexed":false,"name":"tokenId","type":"uint256"},{"indexed":false,"name":"metaId","type":"string"},' \
          '{"indexed":false,"name":"value","type":"uint256"}],"name":"Bought","type":"event"},{"anonymous":false,' \
          '"inputs":[],"name":"Destroy","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,' \
          '"name":"previousOwner","type":"address"},{"indexed":true,"name":"newOwner","type":"address"}],' \
          '"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,' \
          '"name":"account","type":"address"}],"name":"MinterAdded","type":"event"},{"anonymous":false,"inputs":[{' \
          '"indexed":true,"name":"account","type":"address"}],"name":"MinterRemoved","type":"event"},' \
          '{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to",' \
          '"type":"address"},{"indexed":true,"name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},' \
          '{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,' \
          '"name":"approved","type":"address"},{"indexed":true,"name":"tokenId","type":"uint256"}],"name":"Approval",' \
          '"type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},' \
          '{"indexed":true,"name":"operator","type":"address"},{"indexed":false,"name":"approved","type":"bool"}],' \
          '"name":"ApprovalForAll","type":"event"}] '

wrapped_lev_abi = '[{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner",' \
                  '"type":"address"},{"indexed":true,"internalType":"address","name":"spender","type":"address"},' \
                  '{"indexed":false,"internalType":"uint256","name":"value","type":"uint256"}],"name":"Approval",' \
                  '"type":"event"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256",' \
                  '"name":"leviathanID","type":"uint256"}],"name":"LeviathanUnwrapped","type":"event"},' \
                  '{"anonymous":false,"inputs":[{"indexed":false,"internalType":"uint256","name":"leviathanID",' \
                  '"type":"uint256"}],"name":"LeviathanWrapped","type":"event"},{"anonymous":false,"inputs":[{' \
                  '"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,' \
                  '"internalType":"address","name":"to","type":"address"},{"indexed":false,"internalType":"uint256",' \
                  '"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[],' \
                  '"name":"LEVIATHAN","outputs":[{"internalType":"contract IERC721","name":"","type":"address"}],' \
                  '"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"",' \
                  '"type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"_allowance",' \
                  '"outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view",' \
                  '"type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],' \
                  '"name":"_balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],' \
                  '"stateMutability":"view","type":"function"},{"inputs":[],"name":"_totalSupply","outputs":[{' \
                  '"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},' \
                  '{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address",' \
                  '"name":"spender","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256",' \
                  '"name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{' \
                  '"internalType":"address","name":"_spender","type":"address"},{"internalType":"uint256",' \
                  '"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool",' \
                  '"name":"_success","type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{' \
                  '"internalType":"address","name":"account","type":"address"}],"name":"balanceOf","outputs":[{' \
                  '"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},' \
                  '{"inputs":[{"internalType":"uint256","name":"ID","type":"uint256"}],"name":"checkClaim",' \
                  '"outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view",' \
                  '"type":"function"},{"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"",' \
                  '"type":"uint8"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"isPaused",' \
                  '"outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view",' \
                  '"type":"function"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],' \
                  '"name":"leviathans","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],' \
                  '"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{' \
                  '"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},' \
                  '{"inputs":[{"internalType":"address","name":"_from","type":"address"},{"internalType":"uint256",' \
                  '"name":"_tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],' \
                  '"name":"onERC721Received","outputs":[{"internalType":"bytes4","name":"","type":"bytes4"}],' \
                  '"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{' \
                  '"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},' \
                  '{"inputs":[],"name":"pause","outputs":[],"stateMutability":"nonpayable","type":"function"},' \
                  '{"inputs":[{"internalType":"address","name":"_newOwner","type":"address"}],"name":"setOwnership",' \
                  '"outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"symbol",' \
                  '"outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view",' \
                  '"type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256",' \
                  '"name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{' \
                  '"internalType":"address","name":"_to","type":"address"},{"internalType":"uint256","name":"_value",' \
                  '"type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"_success",' \
                  '"type":"bool"}],"stateMutability":"nonpayable","type":"function"},{"inputs":[{' \
                  '"internalType":"address","name":"_from","type":"address"},{"internalType":"address","name":"_to",' \
                  '"type":"address"},{"internalType":"uint256","name":"_value","type":"uint256"}],' \
                  '"name":"transferFrom","outputs":[{"internalType":"bool","name":"_success","type":"bool"}],' \
                  '"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"unpause","outputs":[],' \
                  '"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256",' \
                  '"name":"_amount","type":"uint256"}],"name":"unwrap","outputs":[],"stateMutability":"nonpayable",' \
                  '"type":"function"},{"inputs":[{"internalType":"uint256","name":"_amount","type":"uint256"},' \
                  '{"internalType":"address","name":"_recipient","type":"address"}],"name":"unwrapFor","outputs":[],' \
                  '"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256[]",' \
                  '"name":"_leviathansToWrap","type":"uint256[]"}],"name":"wrap","outputs":[],' \
                  '"stateMutability":"nonpayable","type":"function"}] '

wp_addr = '0x999b1e6EDCb412b59ECF0C5e14c20948Ce81F40b'
surf_addr = '0xEa319e87Cf06203DAe107Dd8E5672175e3Ee976c'
board_addr = '0xf90AeeF57Ae8Bc85FE8d40a3f4a45042F4258c67'
lev_addr = '0xeE52c053e091e8382902E7788Ac27f19bBdFeeDc'
wrapped_lev_addr = '0xA2482ccFF8432ee68b9A26a30fCDd2782Bd81BED'

wp_contract = w3.eth.contract(address=wp_addr, abi=wp_abi)
surf_contract = w3.eth.contract(address=surf_addr, abi=surf_abi)
board_contract = w3.eth.contract(address=board_addr, abi=board_abi)
lev_contract = w3.eth.contract(address=lev_addr, abi=lev_abi)
wrapped_lev_contract = w3.eth.contract(address=wrapped_lev_addr, abi=wrapped_lev_abi)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


def load_address():
    if not os.path.exists("user.json"):
        print("user.json not found, creating one for you!")
        with open("user.json", "w+") as _:
            _.write('{}')
            pass

        return []


def get_addy(user):
    f = open("user.json", "r")
    address = json.load(f)

    try:
        if str(user) in address:
            return address[str(user)]
    except ValueError:
        return False


@bot.command(name='addy')
async def addy(ctx, address):
    user = ctx.author.id
    f = open("user.json", "r")
    users = json.load(f)

    users[str(user)] = address

    try:
        eth_address = EthereumAddress(address)
        json.dump(users, open("./user.json", "w"), indent=4)
        await ctx.send("Successfully set your ethereum address.")
    except ValueError:
        await ctx.send("Invalid ethereum address provided.")



@bot.command(name='info')
async def info(ctx):
    user = ctx.author.id

    wei = 1000000000000000000

    address = get_addy(user)

    # all stats
    surf = surf_contract.functions.balanceOf(address).call()
    board = board_contract.functions.balanceOf(address).call()
    lev_func = lev_contract.functions.tokensOfOwner(address).call()
    board_dividend_balance = surf_contract.functions.balanceOf("0xc456c79213D0d39Fbb2bec1d8Ec356c6d3970A2f").call()

    board_dividends = str(round((board_dividend_balance / 100) / wei, 2))

    surf_balance = str(round(surf / wei, 2))
    # Whirlpool Stuff
    whirlpool = wp_contract.functions.getAllInfoFor(address).call()

    claimable = str(round(whirlpool[1][10] / wei, 2))
    claimed = str(round(whirlpool[1][11] / wei, 2))
    staked = str(round(whirlpool[1][9] / wei, 2))
    total_rewards = str(float(claimable) + float(claimed))

    boards = str(board)
    lev_balance = len(lev_func)
    levs = str(lev_balance)

    embed = discord.Embed(color=0x5ba0d0)
    lev_dividend = 0

    for leviathan_id in lev_func:
        wrapped_lev = wrapped_lev_contract.functions.checkClaim(leviathan_id).call()
        lev_dividend += wrapped_lev
    lev_dividends = str(round(lev_dividend / wei, 2))

    if board >= 1:
        board_holder = "Yes"
    else:
        board_holder = "No"

    if lev_balance >= 1:
        leviathan_holder = "Yes"
    else:
        leviathan_holder = "No"

    embed.add_field(name="Holdings", value="<:surf:812207578409992242> Balance: " + surf_balance + " SURF" +
                                           "\n<:surfboard:812208375802363964> Board Holder? " + board_holder +
                                           "\n<:leviathan:812218767245443072> Lev Holder? " + leviathan_holder,
                    inline=False)

    embed.add_field(name="Whirlpool Rewards", value="\n<:wp:812194248689713153> Claimable: " + claimable + " SURF" +
                                                    "\n<:wp:812194248689713153> Claimed: " + claimed + " SURF" +
                                                    "\n<:wp:812194248689713153> Total Rewards: " + total_rewards +
                                                    " SURF""\n<:wp:812194248689713153> Total Staked: " + staked +
                                                    " SURF/ETH LP", inline=True)
    if board_holder == "Yes":
        embed.add_field(name="Board Stats", value="<:surfboard:812208375802363964> Boards: " + boards +
                                                  "\n<:surfboard:812208375802363964> Claimable Board Dividends: " + str(
            board * board_dividends)
                                                  + " SURF")
    if board_holder and leviathan_holder == "Yes":
        embed.add_field(name="Leviathan Stats", value="<:leviathan:812218767245443072> Leviathans: " + levs +
                                                      "\n<:leviathan:812218767245443072> Claimable Lev Dividends: " + lev_dividends
                                                      + " SURF", inline=False)
    embed.set_author(name="SURF.FINANCE", icon_url="https://i.ibb.co/MGrThQM/logo.png")
    embed.set_thumbnail(url="https://i.ibb.co/MGrThQM/logo.png")

    await ctx.send(embed=embed)

    return None


if __name__ == '__main__':
    load_address()
    bot.run(token)
