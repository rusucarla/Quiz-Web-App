// // import React, { Component } from "react";
// // import Options from "./Option";

// // class Question extends Component {
// //   render() {
// //     const { question, selected, onOptionChange, submit } = this.props;
// //     return (
// //       <div className="">
// //         <h3>Question {question.id}</h3>
// //         <h5 className="mt-2">{question.question}</h5>
// //         <form onSubmit={submit} className="mt-2 mb-2">
// //           {/* Render Options component with necessary props */}
// //           <Options
// //             options={question.options}
// //             selected={selected}
// //             onOptionChange={onOptionChange}
// //           />
// //           <button type="submit" className="btn btn-primary mt-2">Submit</button>
// //         </form>
// //       </div>
// //     );
// //   }
// // }

// // export default Question;


// // Question.js

// import React, {Component} from "react";
// import Options from "./Option";

// class Question extends Component{
//   // constructor(props) {
//   //   super(props);

//   //   // Initialize state if needed
//   //   this.state = {
//   //     // Add state properties here if required
//   //   };
//   // }
// 	render() {
// 		const {question, selectedOption, onOptionChange, onSubmit} = this.props;

// 		return(
// 			<div className="">
// 				<h3>Question {question.id}</h3>
// 				<h5 className="mt-2">{question.question}</h5>
// 				<form onSubmit={onSubmit} className="mt-2 mb-2">
// 					<Options
// 						options={question.options}
// 						selectedOption={selectedOption}
// 						onOptionChange={onOptionChange}
// 					/>
// 					<button type="submit" className="btn btn-primary mt-2">
// 						SUBMIT
// 					</button>
// 				</form>
				
// 			</div>
// 		)
// 	}
// }

// export default Question;
import React, { Component } from "react";
import Options from "./Option";

class Question extends Component {
  render() {
    const { question, selectedOption, onOptionChange, onSubmit } = this.props;

    return (
      <div className="">
        <h3 style={{ fontSize: "24px", color: "blue" }}>Question {question.id}</h3>
        <h5 className="mt-2" style={{ fontSize: "20px", color: "red" }}>{question.question}</h5>
        <form onSubmit={onSubmit} className="mt-2 mb-2">
          <Options
            options={question.options}
            selectedOption={selectedOption}
            onOptionChange={onOptionChange}
          />
          <button type="submit" className="btn btn-primary mt-2">
            SUBMIT
          </button>
        </form>
      </div>
    );
  }
}

export default Question;
