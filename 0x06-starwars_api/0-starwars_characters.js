#!/usr/bin/node
const request = require("request");
const util = require("util");

const promiseR = util.promisify(request);
const [, , id] = process.argv;

const URL = `https://swapi-api.alx-tools.com/api/films/${id}`;

async function fetchData(url) {
  try {
    const bodyData = (await promiseR(url)).body;
    const parsedData = JSON.parse(bodyData);

    for (const char of parsedData.characters) {
      try {
        const charDt = (await promiseR(char)).body;
        const charNm = JSON.parse(charDt).name;
        console.log(charNm);
      } catch (err) {
        console.log(err);
      }
    }
  } catch (err) {
    console.log(err);
  }
}

fetchData(URL);
