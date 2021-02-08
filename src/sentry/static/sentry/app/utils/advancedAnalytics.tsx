import * as qs from 'query-string';

import {Organization} from 'app/types';
import {trackAnalyticsEvent} from 'app/utils/analytics';
import {uniqueId} from 'app/utils/guid';
import {
  EventParameters as IntegrationEventParameters,
  getEventNameMap as getIntegrationEventMap,
} from 'app/utils/integrationUtil';

const ANALYTICS_SESSION = 'ANALYTICS_SESSION' as const;

export const startAnalyticsSession = () => {
  const sessionId = uniqueId();
  window.sessionStorage.setItem(ANALYTICS_SESSION, sessionId);
  return sessionId;
};

export const clearAnalyticsSession = () => {
  window.sessionStorage.removeItem(ANALYTICS_SESSION);
};

export const getAnalyticsSessionId = () =>
  window.sessionStorage.getItem(ANALYTICS_SESSION);

const hasAnalyticsDebug = () => window.localStorage.getItem('DEBUG_ANALYTICS') === '1';

//TODO: add more types
type EventParameters = IntegrationEventParameters;

type AnalyticsKey = keyof EventParameters;

/**
 * Tracks an event for analytics
 * Must be tied to an organization
 * Uses the current session ID or generates a new one if startSession == true
 */
export function trackAdvancedAnalyticsEvent<T extends AnalyticsKey>(
  eventKey: T,
  analyticsParams: EventParameters[T],
  org?: Organization, //we should pass in org whenever we can but not every place guarantees this
  options?: {startSession: boolean},
  mapValuesFn?: (params: object) => object
) {
  const {startSession} = options || {};
  let sessionId = startSession ? startAnalyticsSession() : getAnalyticsSessionId();

  //lazily generate the eventMap
  const allEventMap = {...getIntegrationEventMap()};

  const eventName = allEventMap[eventKey];

  if (!eventName) {
    // eslint-disable-next-line no-console
    console.warn(`Could not find eventName for eventKey ${eventKey}`);
  }

  //we should always have a session id but if we don't, we should generate one
  if (hasAnalyticsDebug() && !sessionId) {
    // eslint-disable-next-line no-console
    console.warn(`analytics_session_id absent from event ${eventKey}`);
    sessionId = startAnalyticsSession();
  }

  let custom_referrer: string | undefined;

  try {
    //pull the referrer from the query parameter of the page
    const {referrer} = qs.parse(window.location.search) || {};
    if (typeof referrer === 'string') {
      // Amplitude has its own referrer which inteferes with our custom referrer
      custom_referrer = referrer;
    }
  } catch {
    // ignore if this fails to parse
    // this can happen if we have an invalid query string
    // e.g. unencoded "%"
  }

  let params = {
    eventKey,
    eventName,
    analytics_session_id: sessionId,
    organization_id: org?.id,
    role: org?.role,
    custom_referrer,
    ...analyticsParams,
  };

  if (mapValuesFn) {
    params = mapValuesFn(params) as any;
  }

  //TODO(steve): remove once we pass in org always
  if (hasAnalyticsDebug() && !org) {
    // eslint-disable-next-line no-console
    console.warn(`Organization absent from event ${eventKey}`);
  }

  //could put this into a debug method or for the main trackAnalyticsEvent event
  if (hasAnalyticsDebug()) {
    // eslint-disable-next-line no-console
    console.log('trackAdvancedAnalytics', params);
  }

  return trackAnalyticsEvent(params);
}
