
"use strict";

let RestartController = require('./RestartController.js')
let SetComplianceMargin = require('./SetComplianceMargin.js')
let SetComplianceSlope = require('./SetComplianceSlope.js')
let SetCompliancePunch = require('./SetCompliancePunch.js')
let StopController = require('./StopController.js')
let StartController = require('./StartController.js')
let SetSpeed = require('./SetSpeed.js')
let SetTorqueLimit = require('./SetTorqueLimit.js')
let TorqueEnable = require('./TorqueEnable.js')

module.exports = {
  RestartController: RestartController,
  SetComplianceMargin: SetComplianceMargin,
  SetComplianceSlope: SetComplianceSlope,
  SetCompliancePunch: SetCompliancePunch,
  StopController: StopController,
  StartController: StartController,
  SetSpeed: SetSpeed,
  SetTorqueLimit: SetTorqueLimit,
  TorqueEnable: TorqueEnable,
};
