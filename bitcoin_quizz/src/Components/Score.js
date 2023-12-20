import React, { Component } from 'react';
import '../App.css'
 
class Score extends Component {
    render() {
        const { score, onNextQuestion } = this.props;
        const isScoreInRange = score >= 5 && score <= 10;
        return (
            <div>
                <h2>Results</h2>
                <h4>Your score: {score}</h4>
                {isScoreInRange ? (
                    <div>
                    <p>Satoshi loves you </p> <br></br>
                    <img src ="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Bitcoin_logo.svg/1024px-Bitcoin_logo.svg.png" alt = "Bitcoin"></img>
                </div>
                ) : (
                    <div>
                        <h4>JesusCoin</h4>
                    <img src ="https://assets.coingecko.com/coins/images/30036/large/JESUS_COIN_LOGO.png?1696528959" alt ="Jesus Coin"></img>
                
                </div>)

                } 

            </div>
        );
    }
}
 
export default Score;