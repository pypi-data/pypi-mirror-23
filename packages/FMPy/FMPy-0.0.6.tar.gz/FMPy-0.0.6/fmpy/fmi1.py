# noinspection PyPep8

import os
import pathlib
import numpy as np
from ctypes import *
from . import free, freeLibrary, platform, sharedLibraryExtension, calloc, CO_SIMULATION, MODEL_EXCHANGE

fmi1Component      = c_void_p
fmi1ValueReference = c_uint
fmi1Real           = c_double
fmi1Integer        = c_int
fmi1Boolean        = c_char
fmi1String         = c_char_p

fmi1True  = b'\x01'
fmi1False = b'\x00'

fmi1UndefinedValueReference = -1

fmi1Status = c_int

fmi1OK      = 0
fmi1Warning = 1
fmi1Discard = 2
fmi1Error   = 3
fmi1Fatal   = 4

fmi1CallbackLoggerTYPE         = CFUNCTYPE(None, fmi1Component, fmi1String, fmi1Status, fmi1String, fmi1String)
fmi1CallbackAllocateMemoryTYPE = CFUNCTYPE(c_void_p, c_size_t, c_size_t)
fmi1CallbackFreeMemoryTYPE     = CFUNCTYPE(None, c_void_p)
# fmi1StepFinishedTYPE           = CFUNCTYPE(None, fmi1Component, fmi1Status)
fmi1StepFinishedTYPE           = c_void_p


def fmi1Call(func):

    def wrapper(self, *args, **kwargs):

        status = func(self, *args, **kwargs)

        if status not in [fmi1OK, fmi1Warning]:
            # TODO: terminate FMU
            # TODO: log this
            values = list(args)
            values += map(lambda it: "%s=%s" % (it[0], it[1]), kwargs.items())
            raise Exception("FMI call %s(%s) returned status %d" % (func.__name__, ', '.join(values), status))

        return status

    return wrapper


class fmi1CallbackFunctions(Structure):
    _fields_ = [('logger',         fmi1CallbackLoggerTYPE),
                ('allocateMemory', fmi1CallbackAllocateMemoryTYPE),
                ('freeMemory',     fmi1CallbackFreeMemoryTYPE),
                ('stepFinished',   fmi1StepFinishedTYPE)]


class fmi1EventInfo(Structure):
    _fields_ = [('iterationConverged',          fmi1Boolean),
                ('stateValueReferencesChanged', fmi1Boolean),
                ('stateValuesChanged',          fmi1Boolean),
                ('terminateSimulation',         fmi1Boolean),
                ('upcomingTimeEvent',           fmi1Boolean),
                ('nextEventTime',               fmi1Real)]


def logger(component, instanceName, status, category, message):
    if status == fmi1Warning:
        print('[WARNING]', message)
    elif status > fmi1Warning:
        print('[ERROR]', message)


def allocateMemory(nobj, size):
    return calloc(nobj, size)


def freeMemory(obj):
    free(obj)


def stepFinished(componentEnvironment, status):
    pass


callbacks = fmi1CallbackFunctions()
callbacks.logger               = fmi1CallbackLoggerTYPE(logger)
callbacks.allocateMemory       = fmi1CallbackAllocateMemoryTYPE(allocateMemory)
callbacks.freeMemory           = fmi1CallbackFreeMemoryTYPE(freeMemory)
#callbacks.stepFinished         = fmi1StepFinishedTYPE(stepFinished)
callbacks.stepFinished = None


class _FMU(object):

    def __init__(self, modelDescription, unzipDirectory, instanceName, fmiType):

        self.modelDescription = modelDescription
        self.unzipDirectory = unzipDirectory
        self.fmiType = fmiType

        if fmiType == MODEL_EXCHANGE:
            self.modelIdentifier = modelDescription.modelExchange.modelIdentifier
        else:
            self.modelIdentifier = modelDescription.coSimulation.modelIdentifier

        self.instanceName = instanceName if instanceName is not None else self.modelIdentifier

        self.fmuLocation = pathlib.Path(self.unzipDirectory).as_uri()

        # remember the current working directory
        work_dir = os.getcwd()

        library_dir = os.path.join(unzipDirectory, 'binaries', platform)

        # change to the library directory as some DLLs expect this to resolve dependencies
        os.chdir(library_dir)

        # load the shared library
        library_path = str(os.path.join(library_dir, self.modelIdentifier + sharedLibraryExtension))
        self.dll = cdll.LoadLibrary(library_path)

        # change back to the working directory
        os.chdir(work_dir)

        self.component = None


class _FMU1(_FMU):

    def __init__(self, modelDescription, unzipDirectory, instanceName, fmiType):

        super(_FMU1, self).__init__(modelDescription, unzipDirectory, instanceName, fmiType)

        # common FMI 1.0 functions
        self.fmi1GetReal             = getattr(self.dll, self.modelIdentifier  + '_fmiGetReal')
        self.fmi1GetReal.argtypes    = [fmi1Component, POINTER(fmi1ValueReference), c_size_t, POINTER(fmi1Real)]
        self.fmi1GetReal.restype     = fmi1Status

        self.fmi1GetInteger          = getattr(self.dll, self.modelIdentifier  + '_fmiGetInteger')
        self.fmi1GetInteger.argtypes = [fmi1Component, POINTER(fmi1ValueReference), c_size_t, POINTER(fmi1Integer)]
        self.fmi1GetInteger.restype  = fmi1Status

        self.fmi1GetBoolean          = getattr(self.dll, self.modelIdentifier  + '_fmiGetBoolean')
        self.fmi1GetBoolean.argtypes = [fmi1Component, POINTER(fmi1ValueReference), c_size_t, POINTER(fmi1Boolean)]
        self.fmi1GetBoolean.restype  = fmi1Status

        self.fmi1GetString           = getattr(self.dll, self.modelIdentifier  + '_fmiGetString')
        self.fmi1GetString.argtypes  = [fmi1Component, POINTER(fmi1ValueReference), c_size_t, POINTER(fmi1String)]
        self.fmi1GetString.restype   = fmi1Status

        self.fmi1SetReal             = getattr(self.dll, self.modelIdentifier  + '_fmiSetReal')
        self.fmi1SetReal.argtypes    = [fmi1Component, POINTER(fmi1ValueReference), c_size_t, POINTER(fmi1Real)]
        self.fmi1SetReal.restype     = fmi1Status

        self.fmi1SetInteger          = getattr(self.dll, self.modelIdentifier  + '_fmiSetInteger')
        self.fmi1SetInteger.argtypes = [fmi1Component, POINTER(fmi1ValueReference), c_size_t, POINTER(fmi1Integer)]
        self.fmi1SetInteger.restype  = fmi1Status

        self.fmi1SetBoolean          = getattr(self.dll, self.modelIdentifier  + '_fmiSetBoolean')
        self.fmi1SetBoolean.argtypes = [fmi1Component, POINTER(fmi1ValueReference), c_size_t, POINTER(fmi1Boolean)]
        self.fmi1SetBoolean.restype  = fmi1Status

        self.fmi1SetString           = getattr(self.dll, self.modelIdentifier  + '_fmiSetString')
        self.fmi1SetString.argtypes  = [fmi1Component, POINTER(fmi1ValueReference), c_size_t, POINTER(fmi1String)]
        self.fmi1SetString.restype   = fmi1Status

    def assertNoError(self, status):
        if status not in [fmi1OK, fmi1Warning]:
            raise Exception("FMI call failed")

    def getReal(self, vr):
        vr = (fmi1ValueReference * len(vr))(*vr)
        value = (fmi1Real * len(vr))()
        status = self.fmi1GetReal(self.component, vr, len(vr), value)
        self.assertNoError(status)
        return list(value)

    def getInteger(self, vr):
        vr = (fmi1ValueReference * len(vr))(*vr)
        value = (fmi1Integer * len(vr))()
        status = self.fmi1GetInteger(self.component, vr, len(vr), value)
        self.assertNoError(status)
        return list(value)

    def getBoolean(self, vr):
        vr = (fmi1ValueReference * len(vr))(*vr)
        value = (fmi1Boolean * len(vr))()
        status = self.fmi1GetBoolean(self.component, vr, len(vr), value)
        self.assertNoError(status)
        return list(map(lambda b: 0 if b == fmi1False else 1, value))

    def getString(self, vr):
        vr = (fmi1ValueReference * len(vr))(*vr)
        value = (fmi1String * len(vr))()
        status = self.fmi1GetString(self.component, vr, len(vr), value)
        self.assertNoError(status)
        return list(value)

    def setReal(self, vr, value):
        vr = (fmi1ValueReference * len(vr))(*vr)
        value = (fmi1Real * len(vr))(*value)
        status = self.fmi1SetReal(self.component, vr, len(vr), value)
        self.assertNoError(status)

    def setInteger(self, vr, value):
        vr = (fmi1ValueReference * len(vr))(*vr)
        value = (fmi1Integer * len(vr))(*value)
        status = self.fmi1SetInteger(self.component, vr, len(vr), value)
        self.assertNoError(status)

    def setBoolean(self, vr, value):
        vr = (fmi1ValueReference * len(vr))(*vr)
        value = (fmi1Boolean * len(vr))(*value)
        status = self.fmi1SetBoolean(self.component, vr, len(vr), value)
        self.assertNoError(status)

    def setString(self, vr, value):
        vr = (fmi1ValueReference * len(vr))(*vr)
        value = map(lambda s: s.encode('utf-8'), value)
        value = (fmi1String * len(vr))(*value)
        status = self.fmi1SetString(self.component, vr, len(vr), value)
        self.assertNoError(status)


class FMU1Slave(_FMU1):

    def __init__(self, modelDescription, unzipDirectory, instanceName=None):

        super(FMU1Slave, self).__init__(modelDescription, unzipDirectory, instanceName, CO_SIMULATION)

        # FMI 1.0 Co-Simulation functions
        self.fmi1InstantiateSlave = getattr(self.dll, self.modelIdentifier + '_fmiInstantiateSlave')
        self.fmi1InstantiateSlave.argtypes = [fmi1String, fmi1String, fmi1String, fmi1String, fmi1Real, fmi1Boolean, fmi1Boolean, fmi1CallbackFunctions, fmi1Boolean]
        self.fmi1InstantiateSlave.restype = fmi1Component

        self.fmi1InitializeSlave = getattr(self.dll, self.modelIdentifier + '_fmiInitializeSlave')
        self.fmi1InitializeSlave.argtypes = [fmi1Component, fmi1Real, fmi1Boolean, fmi1Real]
        self.fmi1InitializeSlave.restype = fmi1Status

        self.fmi1DoStep = getattr(self.dll, self.modelIdentifier + '_fmiDoStep')
        self.fmi1DoStep.argtypes = [fmi1Component, fmi1Real, fmi1Real, fmi1Boolean]
        self.fmi1DoStep.restype = fmi1Status

        self.fmi1TerminateSlave = getattr(self.dll, self.modelIdentifier + '_fmiTerminateSlave')
        self.fmi1TerminateSlave.argtypes = [fmi1Component]
        self.fmi1TerminateSlave.restype = fmi1Status

        self.fmi1FreeSlaveInstance = getattr(self.dll, self.modelIdentifier + '_fmiFreeSlaveInstance')
        self.fmi1FreeSlaveInstance.argtypes = [fmi1Component]
        self.fmi1FreeSlaveInstance.restype = fmi1Status

    def instantiate(self, mimeType='application/x-fmu-sharedlibrary', timeout=0, visible=fmi1False,
                    interactive=fmi1False, functions=callbacks, loggingOn=fmi1False):

        self.component = self.fmi1InstantiateSlave(self.instanceName.encode('UTF-8'),
                                                   self.modelDescription.guid.encode('UTF-8'),
                                                   self.fmuLocation.encode('UTF-8'),
                                                   mimeType.encode('UTF-8'),
                                                   timeout,
                                                   visible,
                                                   interactive,
                                                   functions,
                                                   loggingOn)

    @fmi1Call
    def initialize(self, tStart=0.0, stopTime=None):
        stopTimeDefined = fmi1True if stopTime is not None else fmi1False
        tStop = stopTime if stopTime is not None else 0.0
        return self.fmi1InitializeSlave(self.component, tStart, stopTimeDefined, tStop)

    @fmi1Call
    def terminate(self):
        return self.fmi1TerminateSlave(self.component)

    def freeInstance(self):
        self.fmi1FreeSlaveInstance(self.component)
        # unload the shared library
        freeLibrary(self.dll._handle)

    @fmi1Call
    def doStep(self, currentCommunicationPoint, communicationStepSize, newStep=fmi1True):
        return self.fmi1DoStep(self.component, currentCommunicationPoint, communicationStepSize, newStep)


class FMU1Model(_FMU1):

    def __init__(self, modelDescription, unzipDirectory, instanceName=None):

        super(FMU1Model, self).__init__(modelDescription, unzipDirectory, instanceName, MODEL_EXCHANGE)

        self.eventInfo = fmi1EventInfo()

        nx = modelDescription.numberOfContinuousStates
        nz = modelDescription.numberOfEventIndicators

        self.x = np.zeros(nx)
        self.dx = np.zeros(nx)
        self.z = np.zeros(nz)

        self._px = self.x.ctypes.data_as(POINTER(fmi1Real))
        self._pdx = self.dx.ctypes.data_as(POINTER(fmi1Real))
        self._pz = self.z.ctypes.data_as(POINTER(fmi1Real))

        # FMI 1.0 Model Exchange functions
        self.fmi1InstantiateModel = getattr(self.dll, self.modelIdentifier + '_fmiInstantiateModel')
        self.fmi1InstantiateModel.argtypes = [fmi1String, fmi1String, fmi1CallbackFunctions, fmi1Boolean]
        self.fmi1InstantiateModel.restype = fmi1Component

        self.fmi1SetTime = getattr(self.dll, self.modelIdentifier + '_fmiSetTime')
        self.fmi1SetTime.argtypes = [fmi1Component, fmi1Real]
        self.fmi1SetTime.restype = fmi1Status

        self.fmi1Initialize = getattr(self.dll, self.modelIdentifier + '_fmiInitialize')
        self.fmi1Initialize.argtypes = [fmi1Component, fmi1Boolean, fmi1Real, POINTER(fmi1EventInfo)]
        self.fmi1Initialize.restype = fmi1Status

        self.fmi1GetContinuousStates = getattr(self.dll, self.modelIdentifier + '_fmiGetContinuousStates')
        self.fmi1GetContinuousStates.argtypes = [fmi1Component, POINTER(fmi1Real), c_size_t]
        self.fmi1GetContinuousStates.restype = fmi1Status

        self.fmi1GetDerivatives = getattr(self.dll, self.modelIdentifier + '_fmiGetDerivatives')
        self.fmi1GetDerivatives.argtypes = [fmi1Component, POINTER(fmi1Real), c_size_t]
        self.fmi1GetDerivatives.restype = fmi1Status

        self.fmi1SetContinuousStates = getattr(self.dll, self.modelIdentifier + '_fmiSetContinuousStates')
        self.fmi1SetContinuousStates.argtypes = [fmi1Component, POINTER(fmi1Real), c_size_t]
        self.fmi1SetContinuousStates.restype = fmi1Status

        self.fmi1CompletedIntegratorStep = getattr(self.dll, self.modelIdentifier + '_fmiCompletedIntegratorStep')
        self.fmi1CompletedIntegratorStep.argtypes = [fmi1Component, POINTER(fmi1Boolean)]
        self.fmi1CompletedIntegratorStep.restype = fmi1Status

        self.fmi1GetEventIndicators = getattr(self.dll, self.modelIdentifier + '_fmiGetEventIndicators')
        self.fmi1GetEventIndicators.argtypes = [fmi1Component, POINTER(fmi1Real), c_size_t]
        self.fmi1GetEventIndicators.restype = fmi1Status

        self.fmi1EventUpdate = getattr(self.dll, self.modelIdentifier + '_fmiEventUpdate')
        self.fmi1EventUpdate.argtypes = [fmi1Component, fmi1Boolean, POINTER(fmi1EventInfo)]
        self.fmi1EventUpdate.restype = fmi1Status

        self.fmi1Terminate = getattr(self.dll, self.modelIdentifier + '_fmiTerminate')
        self.fmi1Terminate.argtypes = [fmi1Component]
        self.fmi1Terminate.restype = fmi1Status

        self.fmi1FreeModelInstance = getattr(self.dll, self.modelIdentifier + '_fmiFreeModelInstance')
        self.fmi1FreeModelInstance.argtypes = [fmi1Component]
        self.fmi1FreeModelInstance.restype = fmi1Status

    def instantiate(self, functions=callbacks, loggingOn=fmi1False):
        self.component = self.fmi1InstantiateModel(self.instanceName.encode('UTF-8'),
                                                   self.modelDescription.guid.encode('UTF-8'),
                                                   functions,
                                                   loggingOn)

    @fmi1Call
    def setTime(self, time):
        return self.fmi1SetTime(self.component, time)

    @fmi1Call
    def initialize(self, toleranceControlled=fmi1False, relativeTolerance=0.0):
        return self.fmi1Initialize(self.component, toleranceControlled, relativeTolerance, byref(self.eventInfo))

    @fmi1Call
    def getContinuousStates(self):
        return self.fmi1GetContinuousStates(self.component, self._px, self.x.size)

    @fmi1Call
    def setContinuousStates(self):
        return self.fmi1SetContinuousStates(self.component, self._px, self.x.size)

    @fmi1Call
    def getDerivatives(self):
        return self.fmi1GetDerivatives(self.component, self._pdx, self.dx.size)

    def completedIntegratorStep(self):
        stepEvent = fmi1Boolean()
        status = self.fmi1CompletedIntegratorStep(self.component, byref(stepEvent))
        # TODO: check status
        return stepEvent != fmi1False

    @fmi1Call
    def getEventIndicators(self):
        return self.fmi1GetEventIndicators(self.component, self._pz, self.z.size)

    @fmi1Call
    def eventUpdate(self, intermediateResults=fmi1False):
        return self.fmi1EventUpdate(self.component, intermediateResults, byref(self.eventInfo))

    @fmi1Call
    def terminate(self):
        return self.fmi1Terminate(self.component)

    def freeInstance(self):
        self.fmi1FreeModelInstance(self.component)
        # unload the shared library
        freeLibrary(self.dll._handle)
