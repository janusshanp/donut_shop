var dateEl = document.getElementById('id_date');
	M.Datepicker.init(dateEl, {
	  defaultDate: new Date(),
	  setDefaultDate: true,
	  autoClose: true
	});

// let plusButton = document.getElementById('plus')
// let minusButton = document.getElementById('minus')

// plusButton.addEventListener("click",addFunction)
// minusButton.addEventListener("click",minusFunction)

// function addFunction () {
// 	countEl.textContent = parseInt(countEl.textContent) + parseInt(inputValue.value)
// 	countTextColor()
// }

// function minusFunction () {
// 	countEl.textContent = parseInt(countEl.textContent) - parseInt(inputValue.value)
// 	countTextColor()
// }
