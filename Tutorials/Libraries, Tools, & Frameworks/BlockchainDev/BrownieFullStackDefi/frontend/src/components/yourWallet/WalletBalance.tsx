import { Token } from "../Main";
import { useEthers, useTokenBalance } from "@usedapp/core";
import { formatUnits } from "ethers/lib/utils";
import { makeStyles } from "@material-ui/core";

const useStyles = makeStyles(theme => ({
    container: {
        display: "inline-grid",
        gridTemplateColumns: "auto auto auto",
        gap: theme.spacing(1),
        alignItems: "center"
    },
    tokenImg: {
        width: "32px",
    },
    amount: {
        fontWeight: 700,
    }
}));

export interface WalletBalanceProps {
    token: Token
}

export const WalletBalance = ({ token }: WalletBalanceProps) => {
    const { image, address, name } = token;
    const { account } = useEthers();
    const tokenBalance = useTokenBalance(address, account);
    const formattedTokenBalance: number = tokenBalance ? parseFloat(formatUnits(tokenBalance, 18)) : 0;

    const classes = useStyles();

    return (
        <div className={classes.container}>
            <div>{`You unstaked ${name} balance`}</div>
            <div className={classes.amount}>
                {formattedTokenBalance}
            </div>
            <img className={classes.tokenImg} src={image} alt="token logo" />
        </div>
    );
}