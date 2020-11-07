import React from 'react'
import { Route, Switch } from 'react-router-dom'
import CreateAccountPage from '../../container/CreateAccountPage'
import HomePage from '../../container/HomePage'
import LoginPage from '../../container/LoginPage'
import MarketPage from '../../container/MarketPage'

const Navigation: React.FC = () => {
  return (
    <Switch>
      <Route exact path="/" component={HomePage} />
      <Route exact path="/login" component={LoginPage} />
      <Route exact path="/account/create" component={CreateAccountPage} />
      <Route exact path="/market/:id" component={MarketPage} />
    </Switch>
  )
}

export default Navigation
