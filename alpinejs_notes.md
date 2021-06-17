// notes from alpine.js conference
// HTML: ******************

<div x-data="{ 
    newText: '',
    isProcessing: false,
    people: ['sky stars', 'old school geek', 'sasi'],
    addPerson() {
      this.isProcessing = true;
      this.people.push(this.newText);
      this.newText = '';
      this.isProcessing = false;
             
      // store information into localStorage
    },
    update() {},
    delete() {}
  }" class="min-h-screen bg-blue-100 p-20">

  <!-- form to get new user information -->
  <form @submit.prevent="addPerson">
    <input type="text" x-model="newText" class="p-3 rounded shadow-2xl" />

    <button type="submit" :disabled="isProcessing">
      Add User
    </button>
  </form>

  <!-- loop over the users -->
  <ul class="mt-10">
    <template x-for="person in people">
      <li x-text="person"></li>
    </template>
  </ul>

</div>



// JS: ******************
// starts with vanilla JS, then goes to alpine to show utility:
// // step 1. grab the element
// const btn = document.querySelector("button");

// // step 2. listen for an event on the element
// btn.addEventListener("click", () => {
//   alert("hi there felipe!");
// });

// const input;
// const message;
// const messageOutputArea;

// input.addEventListener
//   messageOutputArea.innerText =

// const form = document.querySelector('');
// const input = document.querySelector('input');

// form.addEventListener('submit', (e) => {
//   e.preventDefault();
//   const newText = input.value;

// })


// step 1. getting dom elements
// step 2. listening for events
// step 3. update the html/dom based on the event