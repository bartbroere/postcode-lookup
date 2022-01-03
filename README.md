# postcode-lookup

Example usage of the API:

```html
<script type="text/javascript">
    let fillStreetCity = function () {
    let postal_code = document.getElementById('postal_code').value
    let house_number = document.getElementById('house_number').value
    let url = new URL('http://postcode/');  // replace this with the location of the Flask app
    url.search = new URLSearchParams({
        postal_code: postal_code,
        house_number: house_number
    }).toString();
    fetch(url).then(response => {
        response.json().then(data => {
            document.getElementById('street').value = data[1]
            document.getElementById('city').value = data[0]
        })
    })
}
</script>
<form>
    <input id="postal_code" name="postal_code" onchange="fillStreetCity()" required>
    <input id="house_number" name="house_number" onchange="fillStreetCity()" required>
    <input id="street" name="street" required>
    <input id="city" name="city" required>
</form>
```
