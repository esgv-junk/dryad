var mathJaxIsLoaded = false

function processMathElement(element) {
}

function processAllMathElements() {
	mathElements = document.getElementsByClassName("math")
	for element in mathElements {
		processMathElement
	}
}