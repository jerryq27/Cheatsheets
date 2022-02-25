import React, { useEffect, useState } from "react";
import { useEthers, useTokenBalance, useNotifications } from "@usedapp/core";
import { formatUnits } from "ethers/lib/utils";
import { utils } from "ethers";
import { Button, CircularProgress, Input, Snackbar } from "@material-ui/core";
import Alert from "@material-ui/lab/Alert";
import { Token } from "../Main"
import { useStakeTokens } from "../../hooks/useStakeTokens";

export interface StakeFormProps {
    token: Token,
}

export const StakeForm = ({ token }: StakeFormProps) => {
    const { address: tokenAddress, name } = token;
    const { account } = useEthers();
    const tokenBalance = useTokenBalance(tokenAddress, account);
    const formattedTokenBalance: number = tokenBalance ? parseFloat(formatUnits(tokenBalance, 18)) : 0;
    const { notifications } = useNotifications();

    const [amount, setAmount] = useState<number | string | Array<number | string>>(0)
    const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        const newAmount = event.target.value === "" ? "" : Number(event.target.value);
        setAmount(newAmount);
        console.log(newAmount);
    }

    const { approveAndStake, state: approveAndStakeErc20State } = useStakeTokens(tokenAddress);
    const handleStakeSubmit = () => {
        const amountAsWei = utils.parseEther(amount.toString())
        return approveAndStake(amountAsWei.toString());
    }

    const isMining = approveAndStakeErc20State.status === "Mining";
    const [showErc20ApprovalSuccess, setShowErc20ApprovalSuccess] = useState(false);
    const [showStakeTokenSucccess, setShowStakeTokenSuccess] = useState(false);
    const handleCloseSnackbar = () => {
        setShowErc20ApprovalSuccess(false);
        setShowStakeTokenSuccess(false);
    };

    // useEffect() watches the variables in the second argument then runs the callback first argument.
    useEffect(() => {
        if (notifications.filter(
            (notification) =>
                notification.type === "transactionSucceed" &&
                notification.transactionName === "Approve ERC20 transfer").length > 0
        ) {
            setShowErc20ApprovalSuccess(true);
            setShowStakeTokenSuccess(false);
        }

        if (notifications.filter(
            (notification) =>
                notification.type === "transactionSucceed" &&
                notification.transactionName === "Stake Tokens").length > 0
        ) {
            setShowErc20ApprovalSuccess(false);
            setShowStakeTokenSuccess(true);
        }
    }, [notifications, showErc20ApprovalSuccess, showStakeTokenSucccess]);

    return (<>
        <div>
            <Input
                onChange={handleInputChange} />
            <Button
                color="primary"
                size="large"
                onClick={handleStakeSubmit}
                disabled={isMining}>
                {isMining ? <CircularProgress size={26} /> : "STAKE!"}
            </Button>
        </div>
        <Snackbar
            open={showErc20ApprovalSuccess}
            autoHideDuration={5000}
            onClose={handleCloseSnackbar}>
            <Alert onClose={handleCloseSnackbar} severity="success">
                ERC20 token transfer approved! Now approve the second transaction.
            </Alert>
        </Snackbar>
        <Snackbar
            open={showStakeTokenSucccess}
            autoHideDuration={5000}
            onClose={handleCloseSnackbar}>
            <Alert onClose={handleCloseSnackbar} severity="success">
                Tokens Staked!
            </Alert>
        </Snackbar>
    </>)
}