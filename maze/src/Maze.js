import React, { Component } from 'react';
import { withStyles } from "@material-ui/core/styles";
import Line from "./Line"
// Material UI
import { Grid, Button } from "@material-ui/core"

const maze = [
    [
        { top: 1, bottom: 0, left: 1, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 0, left: 0, right: 1, center: 0 },
        { top: 1, bottom: 0, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 0, left: 0, right: 1, center: 0 },
        { top: 1, bottom: 0, left: 0, right: 1, center: 3 },
    ],
    [
        { top: 0, bottom: 0, left: 1, right: 1, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 0, bottom: 1, left: 0, right: 1, center: 0 },
        { top: 0, bottom: 0, left: 1, right: 1, center: 0 },
        { top: 1, bottom: 0, left: 1, right: 0, center: 0 },
        { top: 1, bottom: 0, left: 0, right: 1, center: 0 },
        { top: 0, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 0, bottom: 1, left: 0, right: 1, center: 0 },
    ],
    [
        { top: 0, bottom: 0, left: 1, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 0, bottom: 0, left: 0, right: 1, center: 0 },
        { top: 0, bottom: 1, left: 1, right: 1, center: 0 },
        { top: 0, bottom: 0, left: 1, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 0, left: 0, right: 1, center: 0 },
    ],
    [
        { top: 0, bottom: 1, left: 1, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 0, left: 0, right: 1, center: 0 },
        { top: 1, bottom: 1, left: 1, right: 0, center: 0 },
        { top: 0, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 0, bottom: 1, left: 0, right: 1, center: 0 },
        { top: 1, bottom: 0, left: 1, right: 1, center: 0 },
        { top: 0, bottom: 0, left: 0, right: 1, center: 0 },
    ],
    [
        { top: 1, bottom: 0, left: 1, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 1, center: 0 },
        { top: 1, bottom: 0, left: 0, right: 0, center: 0 },
        { top: 0, bottom: 0, left: 0, right: 1, center: 0 },
        { top: 1, bottom: 0, left: 1, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 0, bottom: 1, left: 0, right: 1, center: 0 },
        { top: 0, bottom: 1, left: 0, right: 1, center: 3 },
    ],
    [
        { top: 0, bottom: 1, left: 1, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 0, bottom: 0, left: 0, right: 1, center: 0 },
        { top: 0, bottom: 0, left: 1, right: 0, center: 0 },
        { top: 0, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 0, left: 0, right: 1, center: 0 },

    ],
    [
        { top: 1, bottom: 0, left: 1, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 0, bottom: 1, left: 0, right: 1, center: 0 },
        { top: 0, bottom: 0, left: 1, right: 1, center: 0 },
        { top: 1, bottom: 1, left: 1, right: 0, center: 0 },
        { top: 1, bottom: 0, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 0, left: 0, right: 1, center: 0 },
        { top: 1, bottom: 0, left: 1, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 0, bottom: 1, left: 0, right: 1, center: 0 },
    ],
    [
        { top: 0, bottom: 0, left: 1, right: 0, center: 0 },
        { top: 1, bottom: 0, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 0, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 0, left: 0, right: 0, center: 0 },
        { top: 0, bottom: 0, left: 0, right: 1, center: 0 },
        { top: 0, bottom: 0, left: 1, right: 1, center: 0 },
        { top: 0, bottom: 1, left: 1, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 0, left: 0, right: 1, center: 0 },
    ],
    [
        { top: 0, bottom: 0, left: 1, right: 1, center: 0 },
        { top: 0, bottom: 0, left: 1, right: 1, center: 0 },
        { top: 1, bottom: 1, left: 1, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 1, center: 0 },
        { top: 0, bottom: 0, left: 1, right: 1, center: 0 },
        { top: 0, bottom: 0, left: 1, right: 1, center: 0 },
        { top: 0, bottom: 1, left: 1, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 0, bottom: 0, left: 0, right: 1, center: 0 },
    ],
    [
        { top: 0, bottom: 1, left: 0, right: 1, center: 2 },
        { top: 0, bottom: 1, left: 1, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 0, bottom: 1, left: 0, right: 1, center: 0 },
        { top: 0, bottom: 1, left: 1, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 0, bottom: 1, left: 0, right: 1, center: 0 },
    ],
]

const caminho = ["01", "01", "01", "00", "00", "01", "01", "00", "01", "10", "10", "10", "01", "00", "00", "00", "00", "00", "11", "00", "00", "01", "00", "00", "11", "11"]

const styles = () => ({
    container: {
        padding: 20,
        height: "60vh"
    },

});

class Maze extends Component {
    constructor(props) {
        super(props);

        this.props = props;

        this.state = {
            maze: maze,
            position: [9, 0]
        };

    }

    resetMaze = () => {
        let maze = this.state.maze;
        maze.forEach((arr) => {
            arr.forEach((v) => {
                if (v.center === 4) {
                    v.center = 0
                }
            })
        })
        this.setState({ position: [9, 0] })
        this.setState({ maze: maze })
    }

    mostraCaminho = (caminho) => {
        caminho.forEach((v) => {
            setTimeout(() => {
                switch (v) {
                    case "01":
                        this.moveParaCima()
                        break;
                    case "11":
                        this.moveParaBaixo()
                        break;
                    case "00":
                        this.moveParaDireita()
                        break;
                    case "10":
                        this.moveParaEsquerda()
                        break;
                }
            }, 500);
        })
    }

    moveParaCima = () => {
        let p = this.state.position
        let maze = this.state.maze;
        p = [p[0] - 1, p[1]]

        if (maze[p[0]] !== undefined && maze[p[0]][p[1]] !== undefined) {
            if (maze[p[0]][p[1]].center !== 3) {
                maze[p[0]][p[1]].center = 4
            }

            this.setState({ maze: maze })
            this.setState({ position: p })
        }
    }


    moveParaBaixo = () => {
        let p = this.state.position
        let maze = this.state.maze;
        p = [p[0] + 1, p[1]]
        if (maze[p[0]] !== undefined && maze[p[0]][p[1]] !== undefined) {
            if (maze[p[0]][p[1]].center !== 3) {
                maze[p[0]][p[1]].center = 4
            }
            this.setState({ maze: maze })
            this.setState({ position: p })
        }
    }

    moveParaDireita = () => {
        let p = this.state.position
        let maze = this.state.maze;
        p = [p[0], p[1] + 1]
        if (maze[p[0]] !== undefined && maze[p[0]][p[1]] !== undefined) {
            if (maze[p[0]][p[1]].center !== 3) {
                maze[p[0]][p[1]].center = 4
            }
            this.setState({ maze: maze })
            this.setState({ position: p })
        }
    }

    moveParaEsquerda = () => {
        let p = this.state.position
        let maze = this.state.maze;
        p = [p[0], p[1] - 1]
        if (maze[p[0]] !== undefined && maze[p[0]][p[1]] !== undefined) {
            if (maze[p[0]][p[1]].center !== 3) {
                maze[p[0]][p[1]].center = 4
            }
            this.setState({ maze: maze })
            this.setState({ position: p })
        }
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
                    <Grid container className={classes.container}>
                        <Grid item xs={12}>
                            {this.state.maze.map((v) => {
                                return (<Line line={v}></Line>)
                            })}
                        </Grid>
                    </Grid>
                </Grid>
                <Grid item xs={3}>
                    <Button onClick={() => { this.mostraCaminho(caminho) }}> Teste</Button>
                    <Button onClick={() => { this.resetMaze() }}> Reset</Button>
                </Grid>
            </Grid>);
    }

}

export default withStyles(styles)(Maze);