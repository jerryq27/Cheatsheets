import { useEthers } from "@usedapp/core";
import helperConfig from "../helper-config.json";
import networkMapping from "../chain-info/deployments/map.json";
import brownieConfig from "../brownie-config.json";
import { constants } from "ethers";
import dappImg from "../img/dapp.png";
import wethImg from "../img/eth.png";
import fauImg from "../img/dai.png";
import { YourWallet } from "./yourWallet/YourWallet";
import { makeStyles } from "@material-ui/core";

export type Token = {
    image: string,
    address: string,
    name: string
};

const useStyles = makeStyles((theme) => ({
    title: {
        color: theme.palette.common.white,
        textAlign: "center",
        padding: theme.spacing(4),
    }
}))

export const Main = () => {
    // Show token values from wallet
    // Get the address of different tokens
    // Get the balance of the users wallet

    const classes = useStyles();
    const { chainId } = useEthers();
    const networkName = chainId ? helperConfig[chainId] : "dev"

    const dappTokenAddress = chainId ? networkMapping[String(chainId)]['DappToken'][0] : constants.AddressZero;
    const wethTokenAddress = chainId ? brownieConfig["networks"][networkName]["weth_token"] : constants.AddressZero;
    const fauToken = chainId ? brownieConfig["networks"][networkName]["fau_token"] : constants.AddressZero;

    const supportedTokens: Array<Token> = [
        {
            image: dappImg,
            address: dappTokenAddress,
            name: "DAPP"
        },
        {
            image: wethImg,
            address: wethTokenAddress,
            name: "WETH"
        },
        {
            image: fauImg,
            address: fauToken,
            name: "DAI"
        },
    ];

    return (
        <div>
            <h2 className={classes.title}>Dapp Token App</h2>
            <YourWallet supportedTokens={supportedTokens} />
        </div>
    )
}