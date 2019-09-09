import React, { Component } from 'react';
import { withStyles } from "@material-ui/core/styles";
import Line from "./Line"
// Material UI
import { Grid, Button, Typography,TextField } from "@material-ui/core"
import MazeStore from "./MazeStore"


const maze = [
    [
        { top: 1, bottom: 0, left: 1, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 0, left: 0, right: 1, center: 0 },
        { top: 1, bottom: 0, left: 1, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 0, left: 0, right: 1, center: 0 },
        { top: 1, bottom: 0, left: 1, right: 1, center: 3 },
    ],
    [
        { top: 0, bottom: 0, left: 1, right: 1, center: 0 },
        { top: 1, bottom: 1, left: 1, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 0, bottom: 1, left: 0, right: 1, center: 0 },
        { top: 0, bottom: 0, left: 1, right: 1, center: 0 },
        { top: 1, bottom: 0, left: 1, right: 0, center: 0 },
        { top: 1, bottom: 0, left: 0, right: 1, center: 0 },
        { top: 0, bottom: 1, left: 1, right: 0, center: 0 },
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
        { top: 0, bottom: 0, left: 1, right: 1, center: 0 },
    ],
    [
        { top: 1, bottom: 0, left: 1, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 1, center: 0 },
        { top: 1, bottom: 0, left: 1, right: 0, center: 0 },
        { top: 0, bottom: 0, left: 0, right: 1, center: 0 },
        { top: 1, bottom: 0, left: 1, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 1, bottom: 1, left: 0, right: 0, center: 0 },
        { top: 0, bottom: 1, left: 0, right: 1, center: 0 },
        { top: 0, bottom: 1, left: 1, right: 1, center: 3 },
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
            position: [9, 0],
            score: 0,
            generation: 0,
            params: {},
            stop: true
        };
        this.solved = false
    }


    componentWillMount() {
        this.getParams()
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

    nextGeneration = () => {
        MazeStore.getNextGeneration(this.callBackNext)
    }

    callBackNext = (response) => {
        console.log(response)
        this.setState({ generation: response.generation })
        this.setState({ score: response.score })
        this.resetMaze();
        this.mostraCaminho(response.DNA);
        if (!response.solved && !this.state.stop) {
            setTimeout(() => { MazeStore.getNextGeneration(this.callBackNext) }, 3000);
        }
        //this.mostraCaminho(response.DNA);

    }

    callBackInit = (response) => {
        console.log(response)
        this.setState({ solved: response.solved })
        this.setState({ generation: response.generation })
        this.setState({ score: response.score })
        this.mostraCaminho(response.DNA);
        setTimeout(() => { this.nextGeneration() }, 2000);

    }

    init = () => {
        MazeStore.init(this.callBackInit)
    }

    moveParaCima = () => {
        let p = this.state.position
        let maze = this.state.maze;
        p = [p[0] - 1, p[1]]

        if (maze[p[0]] !== undefined && maze[p[0]][p[1]] !== undefined) {
            if (maze[p[0]][p[1]].center !== 3 && maze[p[0]][p[1]].center !== 2) {
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
            if (maze[p[0]][p[1]].center !== 3 && maze[p[0]][p[1]].center !== 2) {
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
            if (maze[p[0]][p[1]].center !== 3 && maze[p[0]][p[1]].center !== 2) {
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
            if (maze[p[0]][p[1]].center !== 3 && maze[p[0]][p[1]].center !== 2) {
                maze[p[0]][p[1]].center = 4
            }
            this.setState({ maze: maze })
            this.setState({ position: p })
        }
    }

    reset = () => {
        this.setState({ score: 0 })
        this.setState({ generation: 0 })
        this.resetMaze()
    }

    actionButton = () => {
        if (this.state.stop) {
            this.setState({ stop: false }, this.init())
        } else {
            this.setState({ stop: true }, this.reset())
        }
    }

    changeVal = propriety => event => {
        let p = this.state.params
        p[propriety] = event.target.value
        this.setState({ params: p })
    }

    getParams = () => {
        MazeStore.getParams(this.callBackGetParams)
    }

    callBackGetParams = (response) => {
        console.log(response)
        this.setState({ params: response })
    }

    setParams = () => {
        this.setState({stop:true},MazeStore.setParams(()=>{console.log("OK")},this.state.params))
    }

    //Component default methods

    //Event methods

    //Component methods

    //Store methods

    render() {
        const { classes } = this.props;
        return (
            <Grid container>
                <Grid item xs={8}>
                    <Grid container className={classes.container}>
                        <Grid item xs={12}>
                            <Grid container>
                                <Grid item xs={6}>
                                    <Grid container justify="flex-start">
                                        <Typography variant="h4">Geração:{this.state.generation}</Typography>
                                    </Grid>
                                </Grid>
                                <Grid item xs={6}>
                                    <Grid container justify="flex-end">
                                        <Typography variant="h4">Pontuação:{this.state.score}</Typography>
                                    </Grid>
                                </Grid>
                            </Grid>
                        </Grid>
                        <Grid item xs={12}>
                            {this.state.maze.map((v, index) => {
                                return (<Line line={v} key={index}></Line>)
                            })}
                        </Grid>
                    </Grid>
                </Grid>
                <Grid item xs={4}>
                    <form className={classes.formControl} noValidate autoComplete="off">
                        <Grid container>
                            <Grid item xs={6}>
                                <TextField
                                    id="name"
                                    label="Percentual de Crossover"
                                    margin="normal"
                                    value={this.state.params.percentCrossover || 0}
                                    onChange={this.changeVal("percentCrossover")}
                                    className={classes.Input}
                                    fullWidth
                                    required
                                />
                            </Grid>
                            <Grid item xs={6}>
                                <TextField
                                    id="name"
                                    label="Percentual de Mutação"
                                    margin="normal"
                                    value={this.state.params.percentMutation || 0}
                                    onChange={this.changeVal("percentMutation")}
                                    className={classes.Input}
                                    fullWidth
                                    required
                                />
                            </Grid>
                            <Grid item xs={6}>
                                <TextField
                                    id="name"
                                    label="População Máxima"
                                    margin="normal"
                                    value={this.state.params.maxPopulation || 0}
                                    onChange={this.changeVal("maxPopulation")}
                                    className={classes.Input}
                                    fullWidth
                                    required
                                />
                            </Grid>
                            <Grid item xs={6}>
                                <TextField
                                    id="name"
                                    label="Geração Máxima"
                                    margin="normal"
                                    value={this.state.params.maxGenerations || 0}
                                    onChange={this.changeVal("maxGenerations")}
                                    className={classes.Input}
                                    fullWidth
                                    required
                                />
                            </Grid>
                            <Grid item xs={6}>
                                <TextField
                                    id="name"
                                    label="Pontos de Crossover"
                                    margin="normal"
                                    value={this.state.params.crossoverPoints || 0}
                                    onChange={this.changeVal("crossoverPoints")}
                                    className={classes.Input}
                                    fullWidth
                                    required
                                />
                            </Grid>
                            <Grid item xs={6}>
                                <TextField
                                    id="name"
                                    label="Quantidade de Genes Mutáveis"
                                    margin="normal"
                                    value={this.state.params.maxMutation || 0}
                                    onChange={this.changeVal("maxMutation")}
                                    className={classes.Input}
                                    fullWidth
                                    required
                                />
                            </Grid>
                            <Grid item xs={6}>
                                <TextField
                                    id="name"
                                    label="Melhor individuo de"
                                    margin="normal"
                                    value={this.state.params.numberSelection || 0}
                                    onChange={this.changeVal("numberSelection")}
                                    className={classes.Input}
                                    fullWidth
                                    required
                                />
                            </Grid>
                            <Grid item xs={6}>
                                <TextField
                                    id="name"
                                    label="Pontuação parede"
                                    margin="normal"
                                    value={this.state.params.wallPoint || 0}
                                    onChange={this.changeVal("wallPoint")}
                                    className={classes.Input}
                                    fullWidth
                                    required
                                />
                            </Grid>
                            <Grid item xs={6}>
                                <TextField
                                    id="name"
                                    label="Pontuação fora do tabuleiro"
                                    margin="normal"
                                    value={this.state.params.offPoint || 0}
                                    onChange={this.changeVal("offPoint")}
                                    className={classes.Input}
                                    fullWidth
                                    required
                                />
                            </Grid>
                            <Grid item xs={6}>
                                <TextField
                                    id="name"
                                    label="Pontuação por passo"
                                    margin="normal"
                                    value={this.state.params.walkPoint || 0}
                                    onChange={this.changeVal("walkPoint")}
                                    className={classes.Input}
                                    fullWidth
                                    required
                                />
                            </Grid>
                            <Grid item xs={6}>
                                <TextField
                                    id="name"
                                    label="Pontuação chegada ao destino"
                                    margin="normal"
                                    value={this.state.params.goalPoint || 0}
                                    onChange={this.changeVal("goalPoint")}
                                    className={classes.Input}
                                    fullWidth
                                    required
                                />
                            </Grid>
                        </Grid>
                    </form>
                    <Grid container>
                        <Grid item xs={6}>
                            <Grid container justify="flex-start">
                                <Button onClick={this.actionButton}>{this.state.stop?"Iniciar":"Pausar"}</Button>
                            </Grid>
                        </Grid>
                        <Grid item xs={6}>
                            <Grid container justify="flex-end">
                                <Button onClick={this.setParams}>Salvar</Button>
                            </Grid>
                        </Grid>
                    </Grid>
                </Grid>
            </Grid>);
    }

}

export default withStyles(styles)(Maze);