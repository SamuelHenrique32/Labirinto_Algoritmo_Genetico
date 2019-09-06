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
        if(this.props.number.center === 1){
            return "black"
        }else if(this.props.number.center === 2){
            return "green"
        }else if(this.props.number.center === 3){
            return "red"
        }else if(this.props.number.center === 0){
            return "white"
        }else if(this.props.number.center === 4){
            return "yellow"
        }else{
            return "white"
        }
    }

    getMargin = (prop) =>{
        if(this.props.number[prop] === 1){
            return "3px"
        }else{
            return "0px"
        }
    }
    //Store methods

    render() {
        const { classes } = this.props;
        return (
            <Grid container className={classes.cell} 
                style={
                    {
                        backgroundColor:this.getColor(),
                        borderTop:this.getMargin("top"),
                        borderLeft:this.getMargin("left"),
                        borderBottom:this.getMargin("bottom"),
                        borderRight:this.getMargin("right"),
                        borderColor:"black",
                        borderStyle:"solid"
                    }
                }>
            </Grid>
        );
    }

}

export default withStyles(styles)(Cell);