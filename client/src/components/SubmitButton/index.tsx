import React from 'react'
import { Button, CircularProgress } from '@material-ui/core'
import { SubmitButtonProps } from '../../common/interfaces/props'

const SubmitButton = (props: SubmitButtonProps) => {
  return (
    <Button
      startIcon={props.loading ? <CircularProgress size={30} /> : null}
      type="submit"
      fullWidth
      color="primary"
      disabled={props.loading}
    >
      {props.name}
    </Button>
  )
}

export default SubmitButton
