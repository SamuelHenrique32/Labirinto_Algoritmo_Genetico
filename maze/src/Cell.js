import React, { Component } from 'react';
import { withStyles } from "@material-ui/core/styles";

// Material UI
import {Grid} from "@material-ui/core"

const styles = () => ({
    cell:{
        width:"100%",
        height:"100%"
    }
});

class Cell extends Component {
    constructor(props) {
        super(props);

        this.props = props;

        this.state = {
        };
    }

    //Component default methods

    //Event methods

    //Component methods
    getColor = () =>{
        if(this.props.number === 1){
            return "black"
        }else if(this.props.number === 2){
            return "green"
        }else if(this.props.number === 3){
            return "red"
        }else if(this.props.number === 0){
            return "white"
        }else if(this.props.number === 4){
            return "yellow"
        }
    }
    //Store methods

    render() {
        const { classes } = this.props;
        return (
            <Grid container className={classes.cell} style={{backgroundColor:this.getColor()}}>
            </Grid>
        );
    }

}

export default withStyles(styles)(Cell);