import { useState, useEffect } from "react";
import { useContractFunction, useEthers } from "@usedapp/core";
import { constants, Contract, utils } from "ethers";
import TokenFarm from "../chain-info/contracts/TokenFarm.json";
import ERC20 from "../chain-info/contracts/MockDAI.json";
import networkMapping from "../chain-info/deployments/map.json";


export const useStakeTokens = (tokenAddress: string) => {
    // Need address, abit, chainid
    const { chainId } = useEthers();
    const { abi } = TokenFarm;

    const tokenFarmAddress = chainId ? networkMapping[String(chainId)]["TokenFarm"][0] : constants.AddressZero;
    const tokenFarmInterface = new utils.Interface(abi);
    const tokenFarmContract = new Contract(tokenFarmAddress, tokenFarmInterface);

    const erc20abi = ERC20.abi;
    const erc20Interface = new utils.Interface(erc20abi);
    const erc20Contract = new Contract(tokenAddress, erc20Interface);

    // 1. Approve
    const { send: approvedErc20Send, state: approveAndStakeErc20State } = useContractFunction(
        erc20Contract,
        "approve",
        { transactionName: "Approve ERC20 transfer" }
    );

    const approveAndStake = (amount: string) => {
        setAmountToStake(amount);
        return approvedErc20Send(tokenFarmAddress, amount);
    };

    // 2. Stake tokens
    const { send: stakeSend, state: stakeState } = useContractFunction(
        tokenFarmContract,
        "stakeTokens",
        { transactionName: "Stake Tokens" }
    );

    const [amountToStake, setAmountToStake] = useState("0");

    // useEffect() watches the variables in the second argument then runs the callback first argument.
    useEffect(() => {
        if (approveAndStakeErc20State.status === "Success") {
            stakeSend(amountToStake, tokenAddress);
        }
    }, [approveAndStakeErc20State, amountToStake, tokenAddress]);

    const [state, setState] = useState(approveAndStakeErc20State);
    useEffect(() => {
        if (approveAndStakeErc20State.status === "Success") {
            setState(stakeState);
        }
        else {
            setState(approveAndStakeErc20State);
        }
    }, [approveAndStakeErc20State, stakeState]);

    return { approveAndStake, state };
}