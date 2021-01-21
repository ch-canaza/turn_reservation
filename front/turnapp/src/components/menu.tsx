import React from 'react';
import Button from '@material-ui/core/Button';
import Menu from '@material-ui/core/Menu';
import MenuItem from '@material-ui/core/MenuItem';
//import {Redirect} from 'react-router-dom';

export default function SimpleMenu() {
  const [anchorEl, setAnchorEl] = React.useState<null | HTMLElement>(null);
  const [Redirect, setRedirect] = React.useState(false)

  const handleClick = (event: React.MouseEvent<HTMLButtonElement>) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };



  return (
    <div>
      <Button aria-controls="simple-menu" aria-haspopup="true" onClick={handleClick}>
        <h1>Menu</h1>
      </Button>
      <Menu
        id="simple-menu"
        anchorEl={anchorEl}
        keepMounted
        open={Boolean(anchorEl)}
        onClose={handleClose}
      >
        <MenuItem onClick={handleClose}>Home</MenuItem>
        <MenuItem onClick={handleClose}>Create Driver</MenuItem>
        <MenuItem onClick={handleClose}>Upgrade user</MenuItem>
        <MenuItem onClick={handleClose}>User Login</MenuItem>
        <MenuItem onClick={handleClose}>User Logout</MenuItem>
      </Menu>
    </div>
  );
}
