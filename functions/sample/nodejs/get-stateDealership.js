/**MY CODE TO BE USED INSIDE OF IBM CLOUD FUNCTION **/
//Invoke with parameter {"st":"CA"}

const { CloudantV1 } = require("@ibm-cloud/cloudant");
const { IamAuthenticator } = require("ibm-cloud-sdk-core");

function main(params) {
  const authenticator = new IamAuthenticator({
    apikey: "I_AM_API_KEY",
  });
  const cloudant = CloudantV1.newInstance({
    authenticator: authenticator,
  });
  cloudant.setServiceUrl(
    "https://c0973199-be03-41ac-936f-8ee189aea9c2-bluemix.cloudantnosqldb.appdomain.cloud"
  );

  let dbListPromise = getMatchingRecords(cloudant, params);
  return dbListPromise;
}

/*
 Sample implementation to get the records in a db based on a selector. If selector is empty, it returns all records. 
 eg: selector = {state:"Texas"} - Will return all records which has value 'Texas' in the column 'State'
 */

function getMatchingRecords(cloudant, params) {
  return new Promise((resolve, reject) => {
    if (params.st) {
      // return dealership with this state
      cloudant
        .postFind({ db: "dealerships", selector: { st: params.st } })
        .then((result) => {
          // console.log(result.result.docs);
          let code = 200;
          if (result.result.docs.length == 0) {
            code = 404;
          }
          const stateDB = result.result.docs;
          const stateResult = stateDB.map((doc) => {
            return {
              id: doc.id,
              city: doc.city,
              state: doc.state,
              st: doc.st,
              address: doc.address,
              zip: doc.zip,
              lat: doc.lat,
              long: doc.long,
            };
          });
          resolve({
            statusCode: code,
            headers: { "Content-Type": "application/json" },
            body: stateResult,
          });
        })
        .catch((err) => {
          reject({ status: 500, message: "something went wrong on server" });
        });
    } else {
      // return all documents
      cloudant
        .postAllDocs({ db: "dealerships", includeDocs: true, limit: 50 })
        .then((result) => {
          // console.log(result.result.rows);
          let code = 200;
          if (result.result.rows.length == 0) {
            code = 404;
          }
          const dealershipDB = result.result.rows;
          const formatResult = dealershipDB.map((row) => {
            const doc = row.doc;
            return {
              id: doc.id,
              city: doc.city,
              state: doc.state,
              st: doc.st,
              address: doc.address,
              zip: doc.zip,
              lat: doc.lat,
              long: doc.long,
            };
          });
          resolve({
            statusCode: code,
            headers: { "Content-Type": "application/json" },
            body: formatResult,
          });
        })
        .catch((err) => {
          reject({ status: 500, message: "something went wrong on server" });
        });
    }
  });
}