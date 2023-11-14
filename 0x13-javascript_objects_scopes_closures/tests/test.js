#!/usr/bin/node

class Rectangle {
	  constructor (height, width) {
		      this.name = 'Rectangle';
		      this.height = height;
		      this.width = width;
		    }

	  sayName () {
		      console.log(`Hi, I am a ${this.name}.`);
		    }

	  get area () {
		      return this.height * this.width;
		    }

	  set area (value) {
		      this._area = value;
		    }
}
