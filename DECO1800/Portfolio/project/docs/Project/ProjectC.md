---
sidebar: auto
prev: ./ProjectB.md
next: ../reflection/
---

<style>
    p, ul {
        font-family: "Georgia";
    }

</style>


# Project C
This is the last part of Major project. We will produce a final product

## Import Data
Since in partB i made some components but did not put data into it. Therefore in this part, the first stuff i did is to using `ajax` getting data and import them into my component.

### Promise
Considering we use three datas, we would have to call `ajax` three times. Since `ajax` is asynchronous, and because of `javascript` is **single thread**, in order to avoid calling one `ajax` block and delay another calling, the best solution to resolve this is using `es6` syntax [promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise).

`Promise` is `ES6` new feature to deal with asynchronous actions. It is a proxy for a value not necessarily known when the promise is created. It allows developer to associate handlers with an asynchronous action’s eventual success value or failure reason. This let asynchronous methods return values like asynchronous methods: instead of immediately returning the final value, the asynchronous method returns a promise to supply the value at some point in the future.
 
A Promise has three states:
- **Pending**, initial state
- **Fulfilled**: meaning the operation completed successfully
- **Rejected**: meaning the operation failed
  
Our website will only focus on the second state since we want to render the page after data are successfully loaded.
 
To use promise, we first create a Promise object and instead the promise object we using ajax call to get data. After that we could use `.then()` to process data once the state is fulfilled. The promise syntax could be implemented with `Async` syntax to process data.

Here is an example to using `promise` and `ajax` to get data:

```javascript
const mineDataFromSLQ = () => {
    const data = {
        resource_id: '63fd8050-0bab-4c04-b837-b2ce664077bf', // the resource id
        limit: 100,
    }
    return new Promise((resolve, reject) => {
        $.ajax({
            url: 'https://data.gov.au/api/3/action/datastore_search',
            data: data,
            dataType: 'jsonp',
            cache: true,
            success: (data) => {
                resolve(data)
            }
        })
    })
}

// other data

const storeData = (key, data) => {
    records = data.result.records
    window.localStorage.setItem(key, JSON.stringify(records))
}

const getData = () => {
    mineDataFromSLQ()
        .then((data) => {
            storeData('mine', data)
            return convictDataFromSLQ()
        })
        .then((data) => {
            storeData('convict', data)
            return warDataFromSLQ()
        })
        .then((data) => {
            storeData('war', data)
        })
}
```

### Async function
The `async function` declaration defines an **asynchronous function**, which returns an `AsyncFunction` object. An asynchronous function is a function which operates asynchronously via the event loop, using an implicit Promise to return its result. But the syntax and structure of code using async functions is much more like using standard synchronous functions.
 
An async function can contain an await expression that pauses the execution of the async function and waits for the passed Promise's resolution, and then resumes the asyncfunction's execution and returns the resolved value.

::: tip 
`async` and `await` are Syntactic sugar, it makes `javascript` async code looks like mutiple threads processing.
:::

Therefore, the above could also be written in this way:

```javascript
const getDataAsync = async() => {
    mineData = await mineDataFromSLQ()
    convictData = await convictDataFromSLQ()
    warData = await warDataFromSLQ()
}
```

### Element.insertAdjacentHTML()
After getting data from API and storing them locally, we are now able to exract them and insert them to a `div` section. There are serval ways to do that, one way is using `JQuery` `$.html()`. However, currently, the most elegant way to implement this is using `Element.insertAdjacentHTML()` and `template strings` in `ES6`.

Assume the you want to insert your data here:

```html
<div id="dataDiv">
    <!-- data goes here -->
</div>
```

You could do like this:

```javascript
// get data from local first
const DataFromLocal = (name) => {
    warData = window.localStorage.getItem(name)
    data = JSON.parse(warData)
    return data
}

// assume we are using war data
data = warDataFromLocal('war')

let div = document.querySelectorAll('#dataDiv')

// assume we want to insert 3 data records
for (var i = 0; i < 3; i++) {
    let title = data['title']
    const html = `
        <p class="war">title: ${title}</p>
    `
    div.insertAdjacentHTML('beforeend', html)
}
```

This will insert html code with data into the `dataDiv`, the final html code would looks like this:

```html
<div id="dataDiv">
    <p class="war">title: title1</p>
    <p class="war">title: title2</p>
    <p class="war">title: title3</p>
</div>
```

## Final Components

### Flip book
Basically i also added light box effect for this component, this has been taught in week5 tutorial.

Here is the final flip book widget:

![flip final](../images/flip_final.gif)

## New Components

### Typing effect
This is a new component i made at the end, in order to make text more interactive and interesting, i found a thrid party library called [typed.js](https://mattboldt.com/demos/typed-js/). It could generate simulating typing effect with specific text. However, the limitation is that, only one line of text could be displayed, there may be solutions for mutiple text showing, but i did not have time to figure that out.

To set up, create a new `Typed` instance with pointed configuration.

```javascript
const typed = new Typed('.element', {
    strings: ["First sentence.", "Second sentence."],
    typeSpeed: 30
})
```

I combined `mining` data with this effect so that with a given period, a line of mining accident information will be displayed on the screen.

The final demo is showing below:

![typing effect](../images/typing_final.gif)

### Pop up
I also made a `pop up` component for all pages, when user click the button that registered relative events, this effect will be triggered.

The main principle of this effect is to switch `style.display` between `none` and `block`, here is code to implement this:

```javascript
// btn for the trigger button
const btn = document.querySelector('.button')
// span for the close icon at the top
const span = document.querySelector('.x')
// the pop up page
const modal = document.querySelector('.modal');

btn.addEventListener('click', (event) => {
    // initially it is block, once click it, it will be displayed
    modal.style.display = "block";
})

span.addEventListener('click', (event) => {
    modal.style.display = "none"
})

window.addEventListener('click', (event) => {
    // if user click other place in this page, it should be closed as well
    target = event.target
    if (target == modal) {
        modal.style.display = "none"
    }
})
```

The pop up effect runs like this:

![pop up](../images/pop_up.gif)