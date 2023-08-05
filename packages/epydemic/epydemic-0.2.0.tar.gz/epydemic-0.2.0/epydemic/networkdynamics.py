# Networks dynamics simulation base class
#
# Copyright (C) 2017 Simon Dobson
# 
# This file is part of epydemic, epidemic network simulations in Python.
#
# epydemic is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# epydemic is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with epydemic. If not, see <http://www.gnu.org/licenses/gpl.html>.

import epyc
import networkx


class Dynamics(epyc.Experiment, object):
    '''A dynamical process over a network. This is the abstract base class
    for implementing different kinds of dynamics as computational experiments
    suitable for running under. Sub-classes provide synchronous and stochastic
    (Gillespie) simulation dynamics.'''

    # Additional metadata elements
    TIME = 'simulation_time'      #: Metadata element holding the logical simulation end-time.
    EVENTS = 'simulation_events'  #: Metadata element holding the number of events that happened.

    # the default maximum simulation time
    DEFAULT_MAX_TIME = 20000      #: Default maximum simulation time.
    
    def __init__( self, g = None ):
        '''Create a dynamics, optionally initialised to run on the given network.
        The network (if provided) is treated as a prototype that is copied before
        each individual simulation experiment.
        
        :param g: prototype network (optional)'''
        super(Dynamics, self).__init__()
        self._graphPrototype = g
        self._graph = None
        self._maxTime = self.DEFAULT_MAX_TIME

    def network( self ):
        '''Return the network this dynamics is running over.

        :returns: the network'''
        return self._graph

    def setNetworkPrototype( self, g ):
        '''Set the network the dynamics will run over. This will be
        copied for each run of an individual experiment.

        :param g: the network'''
        self._graphPrototype = g

    def setMaximumTime( self, t ):
        '''Set the maximum default simulation time. The default is given
        by :attr:`DEFAULT_MAX_TIME`.

        param: t: the maximum time'''
        self._maxTime = t
        
    def at_equilibrium( self, t ):
        '''Test whether the model is an equilibrium. Override this method to provide
        alternative and/or faster simulations.
        
        :param t: the current simulation timestep
        :returns: True if we're done'''
        return (t >= self._maxTime)

    def setUp( self, params ): 
        '''Before each experiment, create a working copy of the prototype network.

        :param params: parameters of the experiment'''

        # perform the default setup
        super(Dynamics, self).setUp(params)

        # make a copyt of the network prototype
        self._graph = self._graphPrototype.copy()

    def tearDown( self ):
        '''At the end of each experiment, throw away the copy.'''

        # perform the default tear-down
        super(Dynamics, self).tearDown()

        # throw away the worked-on model
        self._graph = None
        
    
