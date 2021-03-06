import {ColumnType, WebVital} from 'app/utils/discover/fields';

export type HistogramData = {
  bin: number;
  count: number;
};

export type Vital = {
  slug: string;
  name: string;
  acronym: string;
  description: string;
  failureThreshold: number;
  type: ColumnType;
};

export type VitalGroup = {
  vitals: WebVital[];
  colors: string[];
  min?: number;
  max?: number;
  precision?: number;
};

export type Point = {
  x: number;
  y: number;
};

export type Rectangle = {
  point1: Point;
  point2: Point;
};

export type DataFilter = 'all' | 'exclude_outliers';
