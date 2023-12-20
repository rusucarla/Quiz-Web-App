// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;

// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;
// import React, { Component } from "react";
// import "bootstrap/dist/css/bootstrap.min.css";
// import Question from "./Components/Question";
// import quests from "./Components/QuestionBank";
// import Score from "./Components/Score";
// import "./App.css";

// class App extends Component {
//   constructor(props) {
//     super(props);
//     this.state = {
//       questionBank: quests,
//       current: 0,
//       select: "",
//       score: 0,
//       ender: false,
//     };

//     // // Binding methods
//     // this.handleOptionChange = this.handleOptionChange.bind(this);
//     // this.submited = this.submited.bind(this);
//     // this.checkAns = this.checkAns.bind(this);
//     // this.NextQ = this.NextQ.bind(this);
//   }

//   handleOptionChange(e) {
//     this.setState({ select: e.target.value });
//   }

//   submited(e) {
//     e.preventDefault();
//     this.checkAns();
//     this.NextQ();
//   }

//   checkAns() {
//     const { questionBank, current, select, score } = this.state;
//     const currentObj = questionBank[current];
//     if (currentObj.hasOwnProperty("answer")) {
//       if (select === currentObj.answer) {
//         this.setState((prevState) => ({
//           score: prevState.score + 1,
//         }));
//       }
//     }
//   }

//   NextQ = () => {
//     const { questionBank, current } = this.state;
//     console.log(questionBank.length);
//     if (current + 1 < questionBank.length) {
//         this.setState((prevState) => ({
//             current: prevState.current + 1,
//             select: "",
//         }));
//     } else {
//         this.setState({
//             ender: true,
//         });
//     }
// };

//   render() {
//     const { questionBank, current, select, score, ender } = this.state;
//     console.log(questionBank.length);
//     return (
//       <div className="App d-flex flex-column align-items-center justify-content-center">
//         <h1 className="app-title">QUIZ APP</h1>
//         {!ender ? (
//           <Question
//             question={questionBank[current]}
//             select={select}
//             onOptionChange={this.handleOptionChange}
//             onSubmit={this.submited}
            
//           />
//         ) : (
          
//           <Score score={score}
//            onNextQuestion={this.NextQ}
//           className="score" />
//         )}
//       </div>
//     );
//   }
// }

// export default App;
// App.js

import React, { Component } from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import Question from "./Components/Question";
import qBank from "./Components/QuestionBank";
import Score from "./Components/Score";
import "./App.css";

class App extends Component {
	constructor(props) {
		super(props);
		this.state = {
			questionBank: qBank,
			current: 0,
			select: "",
			score: 0,
			ender: false,
		};
	}

	handleOptionChange = (e) => {
		this.setState({ select: e.target.value });
	};

	handleFormSubmit = (e) => {
		e.preventDefault();
		this.checkAnswer();
		this.NextQ();
	};

	checkAnswer = () => {
		const { questionBank, current, select, score } = this.state;
    const currentObj = questionBank[current];
    if (currentObj.hasOwnProperty("answer")){
      console.log("are");
      if (select === questionBank[current].answer) {
			this.setState((prevState) => ({ score: prevState.score + 1 }));
      console.log(score);
		}
    }
	if (current === 0) //e prima intrebare
	{
		console.log("hey");
		if (select === "YES")
			this.setState((prevState) => ({ score: prevState.score + 2 }));
		if (select === "i am already rich")
			this.setState((prevState) => ({score: prevState.score + 1}))
	}
	if (current === 1)
	{
		if (select === "angel clean")
			this.setState((prevState) => ({score: prevState.score + 1}));
		if (select === "corporate clean")
			this.setState((prevState) => ({score: prevState.score + 2}));
		if (select === "some like it hot...")
		    this.setState((prevState) => ({score: prevState.score + 3}));
		if (select === "i don't have a soul")
		this.setState((prevState) => ({score: prevState.score + 4}));
		}
	if (current === 4)
	{
		if (select == "My cat is God")
		this.setState((prevState) => ({score: prevState.score + 1}))
	}
		
	};

	NextQ = () => {
		const { questionBank, current } = this.state;
		if (current + 1 < questionBank.length) {
			this.setState((prevState) => ({
				current: prevState.current + 1,
				select: "",
			}));
		} else {
			this.setState({
				ender: true,
			});
		}
	};

	render() {
		const { questionBank, current, select, score, ender } =
			this.state;
		return (
			<div className="App d-flex flex-column align-items-center justify-content-center">
				<h1 className="app-title">QUIZ APP</h1>
				{!ender ? (
          
					<Question
						question={questionBank[current]}
						select={select}
						onOptionChange={this.handleOptionChange}
						onSubmit={this.handleFormSubmit}
					/>
				) : (
					<Score
						score={score}
						onNextQuestion={this.NextQ}
						className="score"
					/>
				)}
			</div>
		);
	}
}

export default App;

