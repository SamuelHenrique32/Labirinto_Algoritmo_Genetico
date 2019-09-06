import React, { Component } from 'react';
import { withStyles } from "@material-ui/core/styles";

// Material UI
import Grid from "@material-ui/core/Grid";
import Cell from "./Cell"
//Prediza 

const styles = () => ({
        line:{
        display:"flex"
    }
});

class Line extends Component {
    constructor(props) {
        super(props);

        this.props = props;

        this.state = {
        };
    }

    //Component default methods

    //Event methods

    //Component methods

    //Store methods

    render() {
        const { classes } = this.props;
        let size = 100/this.props.line.length 
        let t = size.toString() + "%"
        return (
        <Grid item xs={12} className={classes.line} style={{height:size.toString() + "%"}}>
            {this.props.line.map((v)=>{
                return(<Grid container style={{width:size.toString() + "%",height:"100%"}}><Cell number={v}/></Grid>)
            })}
        </Grid>);
    }

}

export default withStyles(styles)(Line);