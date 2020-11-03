//Post products to cart Logic //

const addToCartButton = document.getElementById("addToCartButton")
const product_name = document.getElementById("product_name")
const product_price = document.getElementById("product_price")
const product_quantity = document.getElementById("quantityInput")


const handleSubmit = () => {
    const xhr = new XMLHttpRequest()
    const data = new FormData()
    data.append("product_name" , product_name.textContent)
    data.append("product_price" ,product_price.textContent.split("$")[0])
    data.append("product_quantity" , product_quantity.value)
    xhr.open("POST", "/checkout")
    xhr.send(data)
    alert("Your product has been added successfully to the cart")
  }
  
addToCartButton.addEventListener('click', handleSubmit)




