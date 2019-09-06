import React, { Component } from 'react';
import { withStyles } from "@material-ui/core/styles";
import Line from "./Line"
// Material UI
import { Grid } from "@material-ui/core"

const maze = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1],
    [1, 2, 0, 0, 3, 1],
    [1, 1, 1, 1, 1, 1]
]

const styles = () => ({
    card: {
        width: 10,
        height: 10
    }
});

class Maze extends Component {
    constructor(props) {
        super(props);

        this.props = props;

        this.state = {
            maze: maze
        };

    }

  
    //Component default methods

    //Event methods

    //Component methods

    //Store methods

    render() {
        const { classes } = this.props;
        return (
            <Grid container>
                <Grid item xs={9}>
                    {this.state.maze.map((v)=>{
                        return(<Line line={v}></Line>)
                    })}
                </Grid>
                <Grid item xs={3}>
                   
                </Grid>
            </Grid>);
    }

}

export default withStyles(styles)(Maze);