import React from 'react';
import { Container } from '@material-ui/core';
import { DAppProvider, ChainId } from '@usedapp/core';
import { Header } from './components/Header';
import { Main } from './components/Main';

function App() {
  return (
    <DAppProvider config={{
      supportedChains: [ChainId.Kovan], //, ChainId.Rinkeby, 1337]
      notifications: {
        expirationPeriod: 1000, // Milliseconds(1 second)
        checkInterval: 1000, // Check blockchian every second.
      }
    }}>
      <Header />
      <Container maxWidth="md">
        <div>Hello!</div>
        <Main />
      </Container>
    </DAppProvider>
  );
}

export default App;
