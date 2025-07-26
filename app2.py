"use client";
import React from "react";

function MainComponent() {
  // NIFTY 50 ESG Data (realistic sample data)
  const nifty50Data = [
    {
      id: "nifty_1",
      name: "Reliance Industries",
      sector: "Oil & Gas",
      environmental: {
        score: 72,
        carbonEmissions: 65,
        renewableEnergy: 78,
        wasteManagement: 73,
      },
      social: {
        score: 78,
        employeeSafety: 82,
        diversity: 71,
        communityImpact: 81,
      },
      governance: {
        score: 85,
        boardIndependence: 88,
        executiveComp: 80,
        transparency: 87,
      },
      overallScore: 78,
      isNifty50: true,
    },
    {
      id: "nifty_2",
      name: "TCS",
      sector: "Information Technology",
      environmental: {
        score: 88,
        carbonEmissions: 85,
        renewableEnergy: 92,
        wasteManagement: 87,
      },
      social: {
        score: 91,
        employeeSafety: 89,
        diversity: 94,
        communityImpact: 90,
      },
      governance: {
        score: 93,
        boardIndependence: 95,
        executiveComp: 89,
        transparency: 95,
      },
      overallScore: 91,
      isNifty50: true,
    },
    {
      id: "nifty_3",
      name: "HDFC Bank",
      sector: "Banking",
      environmental: {
        score: 76,
        carbonEmissions: 78,
        renewableEnergy: 72,
        wasteManagement: 78,
      },
      social: {
        score: 84,
        employeeSafety: 86,
        diversity: 79,
        communityImpact: 87,
      },
      governance: {
        score: 89,
        boardIndependence: 92,
        executiveComp: 85,
        transparency: 90,
      },
      overallScore: 83,
      isNifty50: true,
    },
    {
      id: "nifty_4",
      name: "Infosys",
      sector: "Information Technology",
      environmental: {
        score: 86,
        carbonEmissions: 83,
        renewableEnergy: 90,
        wasteManagement: 85,
      },
      social: {
        score: 89,
        employeeSafety: 87,
        diversity: 92,
        communityImpact: 88,
      },
      governance: {
        score: 91,
        boardIndependence: 93,
        executiveComp: 87,
        transparency: 93,
      },
      overallScore: 89,
      isNifty50: true,
    },
    {
      id: "nifty_5",
      name: "ICICI Bank",
      sector: "Banking",
      environmental: {
        score: 74,
        carbonEmissions: 76,
        renewableEnergy: 70,
        wasteManagement: 76,
      },
      social: {
        score: 82,
        employeeSafety: 84,
        diversity: 77,
        communityImpact: 85,
      },
      governance: {
        score: 87,
        boardIndependence: 90,
        executiveComp: 83,
        transparency: 88,
      },
      overallScore: 81,
      isNifty50: true,
    },
    {
      id: "nifty_6",
      name: "Hindustan Unilever",
      sector: "FMCG",
      environmental: {
        score: 91,
        carbonEmissions: 89,
        renewableEnergy: 94,
        wasteManagement: 90,
      },
      social: {
        score: 88,
        employeeSafety: 85,
        diversity: 90,
        communityImpact: 89,
      },
      governance: {
        score: 86,
        boardIndependence: 88,
        executiveComp: 83,
        transparency: 87,
      },
      overallScore: 88,
      isNifty50: true,
    },
    {
      id: "nifty_7",
      name: "ITC",
      sector: "FMCG",
      environmental: {
        score: 79,
        carbonEmissions: 75,
        renewableEnergy: 82,
        wasteManagement: 80,
      },
      social: {
        score: 85,
        employeeSafety: 87,
        diversity: 81,
        communityImpact: 87,
      },
      governance: {
        score: 83,
        boardIndependence: 85,
        executiveComp: 80,
        transparency: 84,
      },
      overallScore: 82,
      isNifty50: true,
    },
    {
      id: "nifty_8",
      name: "Bajaj Finance",
      sector: "Financial Services",
      environmental: {
        score: 71,
        carbonEmissions: 73,
        renewableEnergy: 67,
        wasteManagement: 73,
      },
      social: {
        score: 79,
        employeeSafety: 81,
        diversity: 75,
        communityImpact: 81,
      },
      governance: {
        score: 84,
        boardIndependence: 87,
        executiveComp: 80,
        transparency: 85,
      },
      overallScore: 78,
      isNifty50: true,
    },
    {
      id: "nifty_9",
      name: "Larsen & Toubro",
      sector: "Engineering",
      environmental: {
        score: 73,
        carbonEmissions: 70,
        renewableEnergy: 75,
        wasteManagement: 74,
      },
      social: {
        score: 81,
        employeeSafety: 85,
        diversity: 76,
        communityImpact: 82,
      },
      governance: {
        score: 86,
        boardIndependence: 88,
        executiveComp: 83,
        transparency: 87,
      },
      overallScore: 80,
      isNifty50: true,
    },
    {
      id: "nifty_10",
      name: "Asian Paints",
      sector: "Paints",
      environmental: {
        score: 84,
        carbonEmissions: 81,
        renewableEnergy: 87,
        wasteManagement: 84,
      },
      social: {
        score: 80,
        employeeSafety: 82,
        diversity: 76,
        communityImpact: 82,
      },
      governance: {
        score: 82,
        boardIndependence: 84,
        executiveComp: 79,
        transparency: 83,
      },
      overallScore: 82,
      isNifty50: true,
    },
  ];

  const [companies, setCompanies] = React.useState([]);
  const [selectedCompany, setSelectedCompany] = React.useState(null);
  const [showAddForm, setShowAddForm] = React.useState(false);
  const [activeTab, setActiveTab] = React.useState("nifty50"); // 'nifty50', 'comparison', 'analytics'
  const [newCompany, setNewCompany] = React.useState({
    name: "",
    sector: "",
    environmental: {
      score: 0,
      carbonEmissions: 0,
      renewableEnergy: 0,
      wasteManagement: 0,
    },
    social: { score: 0, employeeSafety: 0, diversity: 0, communityImpact: 0 },
    governance: {
      score: 0,
      boardIndependence: 0,
      executiveComp: 0,
      transparency: 0,
    },
  });

  // Initialize with NIFTY 50 data
  React.useEffect(() => {
    setCompanies(nifty50Data);
  }, []);

  const calculateESGScore = (company) => {
    const envScore =
      (company.environmental.carbonEmissions +
        company.environmental.renewableEnergy +
        company.environmental.wasteManagement) /
      3;
    const socScore =
      (company.social.employeeSafety +
        company.social.diversity +
        company.social.communityImpact) /
      3;
    const govScore =
      (company.governance.boardIndependence +
        company.governance.executiveComp +
        company.governance.transparency) /
      3;

    return {
      environmental: Math.round(envScore),
      social: Math.round(socScore),
      governance: Math.round(govScore),
      overall: Math.round((envScore + socScore + govScore) / 3),
    };
  };

  const addCompany = () => {
    const scores = calculateESGScore(newCompany);
    const companyWithScores = {
      ...newCompany,
      id: "custom_" + Date.now(),
      environmental: {
        ...newCompany.environmental,
        score: scores.environmental,
      },
      social: { ...newCompany.social, score: scores.social },
      governance: { ...newCompany.governance, score: scores.governance },
      overallScore: scores.overall,
      isNifty50: false,
    };

    setCompanies([...companies, companyWithScores]);
    setNewCompany({
      name: "",
      sector: "",
      environmental: {
        score: 0,
        carbonEmissions: 0,
        renewableEnergy: 0,
        wasteManagement: 0,
      },
      social: { score: 0, employeeSafety: 0, diversity: 0, communityImpact: 0 },
      governance: {
        score: 0,
        boardIndependence: 0,
        executiveComp: 0,
        transparency: 0,
      },
    });
    setShowAddForm(false);
  };

  const getScoreColor = (score) => {
    if (score >= 80) return "text-green-600";
    if (score >= 60) return "text-yellow-600";
    return "text-red-600";
  };

  const getScoreBgColor = (score) => {
    if (score >= 80) return "bg-green-100 border-green-200";
    if (score >= 60) return "bg-yellow-100 border-yellow-200";
    return "bg-red-100 border-red-200";
  };

  const getImprovementAreas = (company) => {
    const areas = [];
    if (company.environmental.score < 70)
      areas.push("Environmental practices need improvement");
    if (company.social.score < 70)
      areas.push("Social responsibility initiatives required");
    if (company.governance.score < 70)
      areas.push("Governance structure needs strengthening");
    return areas;
  };

  const nifty50Companies = companies.filter((c) => c.isNifty50);
  const customCompanies = companies.filter((c) => !c.isNifty50);

  const getSectorAnalysis = () => {
    const sectorData = {};
    nifty50Companies.forEach((company) => {
      if (!sectorData[company.sector]) {
        sectorData[company.sector] = {
          count: 0,
          totalESG: 0,
          totalEnv: 0,
          totalSoc: 0,
          totalGov: 0,
        };
      }
      sectorData[company.sector].count += 1;
      sectorData[company.sector].totalESG += company.overallScore;
      sectorData[company.sector].totalEnv += company.environmental.score;
      sectorData[company.sector].totalSoc += company.social.score;
      sectorData[company.sector].totalGov += company.governance.score;
    });

    return Object.entries(sectorData).map(([sector, data]) => ({
      sector,
      avgESG: Math.round(data.totalESG / data.count),
      avgEnv: Math.round(data.totalEnv / data.count),
      avgSoc: Math.round(data.totalSoc / data.count),
      avgGov: Math.round(data.totalGov / data.count),
      count: data.count,
    }));
  };

  const renderBarChart = (data, maxValue = 100) => (
    <div className="relative bg-gray-200 rounded-full h-4">
      <div
        className="absolute top-0 left-0 h-full bg-blue-500 rounded-full transition-all duration-300"
        style={{ width: `${(data / maxValue) * 100}%` }}
      ></div>
      <span className="absolute inset-0 flex items-center justify-center text-xs font-medium text-gray-700">
        {data}
      </span>
    </div>
  );

  const renderTabContent = () => {
    switch (activeTab) {
      case "nifty50":
        return (
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
            <div className="lg:col-span-2">
              <div className="bg-white rounded-lg shadow-lg p-6">
                <h2 className="text-2xl font-semibold text-gray-800 mb-6">
                  NIFTY 50 ESG Rankings
                </h2>
                <div className="overflow-x-auto">
                  <table className="w-full">
                    <thead>
                      <tr className="border-b">
                        <th className="text-left py-3 px-4">Rank</th>
                        <th className="text-left py-3 px-4">Company</th>
                        <th className="text-center py-3 px-4">Environmental</th>
                        <th className="text-center py-3 px-4">Social</th>
                        <th className="text-center py-3 px-4">Governance</th>
                        <th className="text-center py-3 px-4">Overall ESG</th>
                        <th className="text-center py-3 px-4">Action</th>
                      </tr>
                    </thead>
                    <tbody>
                      {nifty50Companies
                        .sort((a, b) => b.overallScore - a.overallScore)
                        .map((company, index) => (
                          <tr
                            key={company.id}
                            className="border-b hover:bg-gray-50"
                          >
                            <td className="py-4 px-4 font-semibold text-gray-600">
                              #{index + 1}
                            </td>
                            <td className="py-4 px-4">
                              <div>
                                <div className="font-semibold">
                                  {company.name}
                                </div>
                                <div className="text-sm text-gray-500">
                                  {company.sector}
                                </div>
                              </div>
                            </td>
                            <td
                              className={`text-center py-4 px-4 font-semibold ${getScoreColor(
                                company.environmental.score
                              )}`}
                            >
                              {company.environmental.score}
                            </td>
                            <td
                              className={`text-center py-4 px-4 font-semibold ${getScoreColor(
                                company.social.score
                              )}`}
                            >
                              {company.social.score}
                            </td>
                            <td
                              className={`text-center py-4 px-4 font-semibold ${getScoreColor(
                                company.governance.score
                              )}`}
                            >
                              {company.governance.score}
                            </td>
                            <td
                              className={`text-center py-4 px-4 font-bold text-lg ${getScoreColor(
                                company.overallScore
                              )}`}
                            >
                              {company.overallScore}
                            </td>
                            <td className="text-center py-4 px-4">
                              <button
                                onClick={() => setSelectedCompany(company)}
                                className="bg-blue-600 text-white px-3 py-1 rounded hover:bg-blue-700 transition-colors text-sm"
                              >
                                Details
                              </button>
                            </td>
                          </tr>
                        ))}
                    </tbody>
                  </table>
                </div>
              </div>
            </div>

            <div className="lg:col-span-1">
              <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
                <h3 className="text-xl font-semibold text-gray-800 mb-4">
                  NIFTY 50 ESG Overview
                </h3>
                <div className="space-y-4">
                  <div
                    className={`p-4 rounded-lg border ${getScoreBgColor(
                      nifty50Companies.reduce(
                        (acc, c) => acc + c.overallScore,
                        0
                      ) / nifty50Companies.length
                    )}`}
                  >
                    <div className="text-sm text-gray-600">
                      Average ESG Score
                    </div>
                    <div className="text-2xl font-bold">
                      {Math.round(
                        nifty50Companies.reduce(
                          (acc, c) => acc + c.overallScore,
                          0
                        ) / nifty50Companies.length
                      )}
                    </div>
                  </div>
                  <div className="grid grid-cols-3 gap-2">
                    <div className="text-center p-3 bg-green-50 rounded">
                      <div className="text-xs text-gray-600">ENV</div>
                      <div className="font-semibold">
                        {Math.round(
                          nifty50Companies.reduce(
                            (acc, c) => acc + c.environmental.score,
                            0
                          ) / nifty50Companies.length
                        )}
                      </div>
                    </div>
                    <div className="text-center p-3 bg-blue-50 rounded">
                      <div className="text-xs text-gray-600">SOC</div>
                      <div className="font-semibold">
                        {Math.round(
                          nifty50Companies.reduce(
                            (acc, c) => acc + c.social.score,
                            0
                          ) / nifty50Companies.length
                        )}
                      </div>
                    </div>
                    <div className="text-center p-3 bg-purple-50 rounded">
                      <div className="text-xs text-gray-600">GOV</div>
                      <div className="font-semibold">
                        {Math.round(
                          nifty50Companies.reduce(
                            (acc, c) => acc + c.governance.score,
                            0
                          ) / nifty50Companies.length
                        )}
                      </div>
                    </div>
                  </div>
                </div>
              </div>

              {selectedCompany && (
                <div className="bg-white rounded-lg shadow-lg p-6">
                  <h3 className="text-xl font-semibold text-gray-800 mb-4">
                    Company Analysis
                  </h3>
                  <div className="mb-6">
                    <h4 className="font-semibold text-lg">
                      {selectedCompany.name}
                    </h4>
                    <p className="text-gray-600">{selectedCompany.sector}</p>
                    <div
                      className={`text-2xl font-bold mt-2 ${getScoreColor(
                        selectedCompany.overallScore
                      )}`}
                    >
                      ESG Score: {selectedCompany.overallScore}/100
                    </div>
                    {selectedCompany.isNifty50 && (
                      <span className="inline-block bg-blue-100 text-blue-800 text-xs px-2 py-1 rounded-full mt-2">
                        NIFTY 50
                      </span>
                    )}
                  </div>

                  <div className="space-y-4">
                    <div>
                      <div className="flex justify-between items-center mb-2">
                        <span className="font-medium">Environmental</span>
                        <span
                          className={`font-semibold ${getScoreColor(
                            selectedCompany.environmental.score
                          )}`}
                        >
                          {selectedCompany.environmental.score}
                        </span>
                      </div>
                      {renderBarChart(selectedCompany.environmental.score)}
                    </div>

                    <div>
                      <div className="flex justify-between items-center mb-2">
                        <span className="font-medium">Social</span>
                        <span
                          className={`font-semibold ${getScoreColor(
                            selectedCompany.social.score
                          )}`}
                        >
                          {selectedCompany.social.score}
                        </span>
                      </div>
                      {renderBarChart(selectedCompany.social.score)}
                    </div>

                    <div>
                      <div className="flex justify-between items-center mb-2">
                        <span className="font-medium">Governance</span>
                        <span
                          className={`font-semibold ${getScoreColor(
                            selectedCompany.governance.score
                          )}`}
                        >
                          {selectedCompany.governance.score}
                        </span>
                      </div>
                      {renderBarChart(selectedCompany.governance.score)}
                    </div>
                  </div>

                  <div className="mt-6">
                    <h5 className="font-semibold mb-3">
                      Areas for Improvement
                    </h5>
                    <div className="space-y-2">
                      {getImprovementAreas(selectedCompany).map(
                        (area, index) => (
                          <div
                            key={index}
                            className="bg-yellow-50 border-l-4 border-yellow-400 p-3"
                          >
                            <p className="text-sm text-yellow-800">{area}</p>
                          </div>
                        )
                      )}
                      {getImprovementAreas(selectedCompany).length === 0 && (
                        <div className="bg-green-50 border-l-4 border-green-400 p-3">
                          <p className="text-sm text-green-800">
                            Strong performance across all ESG categories
                          </p>
                        </div>
                      )}
                    </div>
                  </div>
                </div>
              )}
            </div>
          </div>
        );

      case "comparison":
        return (
          <div className="space-y-8">
            <div className="flex justify-between items-center">
              <h2 className="text-2xl font-semibold text-gray-800">
                Company Comparison with NIFTY 50
              </h2>
              <button
                onClick={() => setShowAddForm(true)}
                className="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700 transition-colors"
              >
                Add New Company
              </button>
            </div>

            {customCompanies.length === 0 ? (
              <div className="bg-white rounded-lg shadow-lg p-12 text-center">
                <i className="fas fa-plus-circle text-4xl text-gray-400 mb-4"></i>
                <p className="text-gray-500 text-lg mb-4">
                  No custom companies added yet
                </p>
                <p className="text-gray-400">
                  Add your company to compare it with NIFTY 50 leaders
                </p>
              </div>
            ) : (
              <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
                {customCompanies.map((company) => {
                  const niftyAvg = Math.round(
                    nifty50Companies.reduce(
                      (acc, c) => acc + c.overallScore,
                      0
                    ) / nifty50Companies.length
                  );
                  const sectorCompanies = nifty50Companies.filter(
                    (c) => c.sector === company.sector
                  );
                  const sectorAvg =
                    sectorCompanies.length > 0
                      ? Math.round(
                          sectorCompanies.reduce(
                            (acc, c) => acc + c.overallScore,
                            0
                          ) / sectorCompanies.length
                        )
                      : niftyAvg;

                  return (
                    <div
                      key={company.id}
                      className="bg-white rounded-lg shadow-lg p-6"
                    >
                      <div className="mb-6">
                        <h3 className="text-xl font-semibold">
                          {company.name}
                        </h3>
                        <p className="text-gray-600">{company.sector}</p>
                      </div>

                      <div className="space-y-4">
                        <div className="grid grid-cols-3 gap-4 text-center">
                          <div
                            className={`p-3 rounded ${getScoreBgColor(
                              company.overallScore
                            )}`}
                          >
                            <div className="text-sm text-gray-600">
                              Your Score
                            </div>
                            <div
                              className={`text-xl font-bold ${getScoreColor(
                                company.overallScore
                              )}`}
                            >
                              {company.overallScore}
                            </div>
                          </div>
                          <div className="p-3 rounded bg-blue-50 border border-blue-200">
                            <div className="text-sm text-gray-600">
                              Sector Avg
                            </div>
                            <div className="text-xl font-bold text-blue-600">
                              {sectorAvg}
                            </div>
                          </div>
                          <div className="p-3 rounded bg-gray-50 border border-gray-200">
                            <div className="text-sm text-gray-600">
                              NIFTY 50 Avg
                            </div>
                            <div className="text-xl font-bold text-gray-600">
                              {niftyAvg}
                            </div>
                          </div>
                        </div>

                        <div className="space-y-3">
                          <div>
                            <div className="flex justify-between text-sm mb-1">
                              <span>Environmental</span>
                              <span>
                                {company.environmental.score} vs{" "}
                                {Math.round(
                                  nifty50Companies.reduce(
                                    (acc, c) => acc + c.environmental.score,
                                    0
                                  ) / nifty50Companies.length
                                )}
                              </span>
                            </div>
                            <div className="flex space-x-1">
                              <div className="flex-1 bg-gray-200 rounded-full h-2">
                                <div
                                  className="bg-green-500 h-2 rounded-full"
                                  style={{
                                    width: `${company.environmental.score}%`,
                                  }}
                                ></div>
                              </div>
                              <div className="flex-1 bg-gray-200 rounded-full h-2">
                                <div
                                  className="bg-gray-400 h-2 rounded-full"
                                  style={{
                                    width: `${Math.round(
                                      nifty50Companies.reduce(
                                        (acc, c) => acc + c.environmental.score,
                                        0
                                      ) / nifty50Companies.length
                                    )}%`,
                                  }}
                                ></div>
                              </div>
                            </div>
                          </div>

                          <div>
                            <div className="flex justify-between text-sm mb-1">
                              <span>Social</span>
                              <span>
                                {company.social.score} vs{" "}
                                {Math.round(
                                  nifty50Companies.reduce(
                                    (acc, c) => acc + c.social.score,
                                    0
                                  ) / nifty50Companies.length
                                )}
                              </span>
                            </div>
                            <div className="flex space-x-1">
                              <div className="flex-1 bg-gray-200 rounded-full h-2">
                                <div
                                  className="bg-blue-500 h-2 rounded-full"
                                  style={{ width: `${company.social.score}%` }}
                                ></div>
                              </div>
                              <div className="flex-1 bg-gray-200 rounded-full h-2">
                                <div
                                  className="bg-gray-400 h-2 rounded-full"
                                  style={{
                                    width: `${Math.round(
                                      nifty50Companies.reduce(
                                        (acc, c) => acc + c.social.score,
                                        0
                                      ) / nifty50Companies.length
                                    )}%`,
                                  }}
                                ></div>
                              </div>
                            </div>
                          </div>

                          <div>
                            <div className="flex justify-between text-sm mb-1">
                              <span>Governance</span>
                              <span>
                                {company.governance.score} vs{" "}
                                {Math.round(
                                  nifty50Companies.reduce(
                                    (acc, c) => acc + c.governance.score,
                                    0
                                  ) / nifty50Companies.length
                                )}
                              </span>
                            </div>
                            <div className="flex space-x-1">
                              <div className="flex-1 bg-gray-200 rounded-full h-2">
                                <div
                                  className="bg-purple-500 h-2 rounded-full"
                                  style={{
                                    width: `${company.governance.score}%`,
                                  }}
                                ></div>
                              </div>
                              <div className="flex-1 bg-gray-200 rounded-full h-2">
                                <div
                                  className="bg-gray-400 h-2 rounded-full"
                                  style={{
                                    width: `${Math.round(
                                      nifty50Companies.reduce(
                                        (acc, c) => acc + c.governance.score,
                                        0
                                      ) / nifty50Companies.length
                                    )}%`,
                                  }}
                                ></div>
                              </div>
                            </div>
                          </div>
                        </div>

                        <div className="mt-4 p-3 bg-gray-50 rounded">
                          <div className="text-sm font-medium mb-2">
                            Performance Summary:
                          </div>
                          <div className="text-sm text-gray-600">
                            {company.overallScore > niftyAvg
                              ? `✅ Above NIFTY 50 average by ${
                                  company.overallScore - niftyAvg
                                } points`
                              : `⚠️ Below NIFTY 50 average by ${
                                  niftyAvg - company.overallScore
                                } points`}
                          </div>
                        </div>
                      </div>
                    </div>
                  );
                })}
              </div>
            )}
          </div>
        );

      case "analytics":
        const sectorAnalysis = getSectorAnalysis();
        return (
          <div className="space-y-8">
            <h2 className="text-2xl font-semibold text-gray-800">
              NIFTY 50 ESG Analytics
            </h2>

            <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
              <div className="bg-white rounded-lg shadow-lg p-6">
                <h3 className="text-xl font-semibold mb-4">
                  Sector-wise ESG Performance
                </h3>
                <div className="space-y-4">
                  {sectorAnalysis.map((sector) => (
                    <div key={sector.sector} className="p-4 border rounded-lg">
                      <div className="flex justify-between items-center mb-2">
                        <span className="font-medium">{sector.sector}</span>
                        <span className="text-sm text-gray-500">
                          ({sector.count} companies)
                        </span>
                      </div>
                      <div className="mb-2">
                        <div className="flex justify-between text-sm mb-1">
                          <span>Average ESG Score</span>
                          <span
                            className={`font-semibold ${getScoreColor(
                              sector.avgESG
                            )}`}
                          >
                            {sector.avgESG}
                          </span>
                        </div>
                        {renderBarChart(sector.avgESG)}
                      </div>
                      <div className="grid grid-cols-3 gap-2 text-xs">
                        <div className="text-center">
                          <div className="text-gray-500">ENV</div>
                          <div className={getScoreColor(sector.avgEnv)}>
                            {sector.avgEnv}
                          </div>
                        </div>
                        <div className="text-center">
                          <div className="text-gray-500">SOC</div>
                          <div className={getScoreColor(sector.avgSoc)}>
                            {sector.avgSoc}
                          </div>
                        </div>
                        <div className="text-center">
                          <div className="text-gray-500">GOV</div>
                          <div className={getScoreColor(sector.avgGov)}>
                            {sector.avgGov}
                          </div>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>

              <div className="bg-white rounded-lg shadow-lg p-6">
                <h3 className="text-xl font-semibold mb-4">
                  Top & Bottom Performers
                </h3>
                <div className="space-y-6">
                  <div>
                    <h4 className="font-medium text-green-600 mb-3">
                      🏆 Top 5 ESG Leaders
                    </h4>
                    <div className="space-y-2">
                      {nifty50Companies
                        .sort((a, b) => b.overallScore - a.overallScore)
                        .slice(0, 5)
                        .map((company, index) => (
                          <div
                            key={company.id}
                            className="flex justify-between items-center p-2 bg-green-50 rounded"
                          >
                            <div>
                              <span className="font-medium">
                                #{index + 1} {company.name}
                              </span>
                              <div className="text-xs text-gray-500">
                                {company.sector}
                              </div>
                            </div>
                            <span className="font-bold text-green-600">
                              {company.overallScore}
                            </span>
                          </div>
                        ))}
                    </div>
                  </div>

                  <div>
                    <h4 className="font-medium text-red-600 mb-3">
                      📉 Bottom 5 - Improvement Needed
                    </h4>
                    <div className="space-y-2">
                      {nifty50Companies
                        .sort((a, b) => a.overallScore - b.overallScore)
                        .slice(0, 5)
                        .map((company, index) => (
                          <div
                            key={company.id}
                            className="flex justify-between items-center p-2 bg-red-50 rounded"
                          >
                            <div>
                              <span className="font-medium">
                                {company.name}
                              </span>
                              <div className="text-xs text-gray-500">
                                {company.sector}
                              </div>
                            </div>
                            <span className="font-bold text-red-600">
                              {company.overallScore}
                            </span>
                          </div>
                        ))}
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        );

      default:
        return null;
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 p-4 md:p-8">
      <div className="max-w-7xl mx-auto">
        <div className="bg-white rounded-lg shadow-lg p-6 mb-8">
          <h1 className="text-3xl font-bold text-gray-800 mb-2">
            NIFTY 50 ESG Analytics Dashboard
          </h1>
          <p className="text-gray-600">
            Comprehensive ESG analysis and comparison tool for NIFTY 50
            companies and your portfolio
          </p>
        </div>

        {/* Tab Navigation */}
        <div className="bg-white rounded-lg shadow-lg mb-8">
          <div className="flex border-b">
            <button
              onClick={() => setActiveTab("nifty50")}
              className={`px-6 py-4 font-medium transition-colors ${
                activeTab === "nifty50"
                  ? "text-blue-600 border-b-2 border-blue-600 bg-blue-50"
                  : "text-gray-500 hover:text-gray-700"
              }`}
            >
              <i className="fas fa-chart-line mr-2"></i>
              NIFTY 50 Rankings
            </button>
            <button
              onClick={() => setActiveTab("comparison")}
              className={`px-6 py-4 font-medium transition-colors ${
                activeTab === "comparison"
                  ? "text-blue-600 border-b-2 border-blue-600 bg-blue-50"
                  : "text-gray-500 hover:text-gray-700"
              }`}
            >
              <i className="fas fa-balance-scale mr-2"></i>
              Company Comparison
            </button>
            <button
              onClick={() => setActiveTab("analytics")}
              className={`px-6 py-4 font-medium transition-colors ${
                activeTab === "analytics"
                  ? "text-blue-600 border-b-2 border-blue-600 bg-blue-50"
                  : "text-gray-500 hover:text-gray-700"
              }`}
            >
              <i className="fas fa-analytics mr-2"></i>
              Sector Analytics
            </button>
          </div>

          <div className="p-6">{renderTabContent()}</div>
        </div>

        {/* Add Company Modal */}
        {showAddForm && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
            <div className="bg-white rounded-lg p-6 w-full max-w-2xl max-h-[90vh] overflow-y-auto">
              <div className="flex justify-between items-center mb-6">
                <h3 className="text-xl font-semibold">
                  Add New Company for NIFTY 50 Comparison
                </h3>
                <button
                  onClick={() => setShowAddForm(false)}
                  className="text-gray-500 hover:text-gray-700"
                >
                  <i className="fas fa-times text-xl"></i>
                </button>
              </div>

              <div className="space-y-6">
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium mb-2">
                      Company Name
                    </label>
                    <input
                      type="text"
                      value={newCompany.name}
                      onChange={(e) =>
                        setNewCompany({ ...newCompany, name: e.target.value })
                      }
                      className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent"
                      placeholder="Enter company name"
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium mb-2">
                      Sector
                    </label>
                    <select
                      value={newCompany.sector}
                      onChange={(e) =>
                        setNewCompany({ ...newCompany, sector: e.target.value })
                      }
                      className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent"
                    >
                      <option value="">Select sector</option>
                      <option value="Information Technology">
                        Information Technology
                      </option>
                      <option value="Banking">Banking</option>
                      <option value="FMCG">FMCG</option>
                      <option value="Financial Services">
                        Financial Services
                      </option>
                      <option value="Oil & Gas">Oil & Gas</option>
                      <option value="Engineering">Engineering</option>
                      <option value="Paints">Paints</option>
                      <option value="Other">Other</option>
                    </select>
                  </div>
                </div>

                {/* Environmental Scores */}
                <div>
                  <h4 className="font-semibold text-green-700 mb-3">
                    Environmental Factors (0-100)
                  </h4>
                  <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div>
                      <label className="block text-sm font-medium mb-2">
                        Carbon Emissions
                      </label>
                      <input
                        type="number"
                        min="0"
                        max="100"
                        value={newCompany.environmental.carbonEmissions}
                        onChange={(e) =>
                          setNewCompany({
                            ...newCompany,
                            environmental: {
                              ...newCompany.environmental,
                              carbonEmissions: parseInt(e.target.value) || 0,
                            },
                          })
                        }
                        className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent"
                      />
                    </div>
                    <div>
                      <label className="block text-sm font-medium mb-2">
                        Renewable Energy
                      </label>
                      <input
                        type="number"
                        min="0"
                        max="100"
                        value={newCompany.environmental.renewableEnergy}
                        onChange={(e) =>
                          setNewCompany({
                            ...newCompany,
                            environmental: {
                              ...newCompany.environmental,
                              renewableEnergy: parseInt(e.target.value) || 0,
                            },
                          })
                        }
                        className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent"
                      />
                    </div>
                    <div>
                      <label className="block text-sm font-medium mb-2">
                        Waste Management
                      </label>
                      <input
                        type="number"
                        min="0"
                        max="100"
                        value={newCompany.environmental.wasteManagement}
                        onChange={(e) =>
                          setNewCompany({
                            ...newCompany,
                            environmental: {
                              ...newCompany.environmental,
                              wasteManagement: parseInt(e.target.value) || 0,
                            },
                          })
                        }
                        className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent"
                      />
                    </div>
                  </div>
                </div>

                {/* Social Scores */}
                <div>
                  <h4 className="font-semibold text-blue-700 mb-3">
                    Social Factors (0-100)
                  </h4>
                  <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div>
                      <label className="block text-sm font-medium mb-2">
                        Employee Safety
                      </label>
                      <input
                        type="number"
                        min="0"
                        max="100"
                        value={newCompany.social.employeeSafety}
                        onChange={(e) =>
                          setNewCompany({
                            ...newCompany,
                            social: {
                              ...newCompany.social,
                              employeeSafety: parseInt(e.target.value) || 0,
                            },
                          })
                        }
                        className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                      />
                    </div>
                    <div>
                      <label className="block text-sm font-medium mb-2">
                        Diversity & Inclusion
                      </label>
                      <input
                        type="number"
                        min="0"
                        max="100"
                        value={newCompany.social.diversity}
                        onChange={(e) =>
                          setNewCompany({
                            ...newCompany,
                            social: {
                              ...newCompany.social,
                              diversity: parseInt(e.target.value) || 0,
                            },
                          })
                        }
                        className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                      />
                    </div>
                    <div>
                      <label className="block text-sm font-medium mb-2">
                        Community Impact
                      </label>
                      <input
                        type="number"
                        min="0"
                        max="100"
                        value={newCompany.social.communityImpact}
                        onChange={(e) =>
                          setNewCompany({
                            ...newCompany,
                            social: {
                              ...newCompany.social,
                              communityImpact: parseInt(e.target.value) || 0,
                            },
                          })
                        }
                        className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                      />
                    </div>
                  </div>
                </div>

                {/* Governance Scores */}
                <div>
                  <h4 className="font-semibold text-purple-700 mb-3">
                    Governance Factors (0-100)
                  </h4>
                  <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div>
                      <label className="block text-sm font-medium mb-2">
                        Board Independence
                      </label>
                      <input
                        type="number"
                        min="0"
                        max="100"
                        value={newCompany.governance.boardIndependence}
                        onChange={(e) =>
                          setNewCompany({
                            ...newCompany,
                            governance: {
                              ...newCompany.governance,
                              boardIndependence: parseInt(e.target.value) || 0,
                            },
                          })
                        }
                        className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent"
                      />
                    </div>
                    <div>
                      <label className="block text-sm font-medium mb-2">
                        Executive Compensation
                      </label>
                      <input
                        type="number"
                        min="0"
                        max="100"
                        value={newCompany.governance.executiveComp}
                        onChange={(e) =>
                          setNewCompany({
                            ...newCompany,
                            governance: {
                              ...newCompany.governance,
                              executiveComp: parseInt(e.target.value) || 0,
                            },
                          })
                        }
                        className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent"
                      />
                    </div>
                    <div>
                      <label className="block text-sm font-medium mb-2">
                        Transparency
                      </label>
                      <input
                        type="number"
                        min="0"
                        max="100"
                        value={newCompany.governance.transparency}
                        onChange={(e) =>
                          setNewCompany({
                            ...newCompany,
                            governance: {
                              ...newCompany.governance,
                              transparency: parseInt(e.target.value) || 0,
                            },
                          })
                        }
                        className="w-full p-3 border rounded-lg focus:ring-2 focus:ring-purple-500 focus:border-transparent"
                      />
                    </div>
                  </div>
                </div>

                <div className="flex justify-end space-x-4 pt-4">
                  <button
                    onClick={() => setShowAddForm(false)}
                    className="px-6 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors"
                  >
                    Cancel
                  </button>
                  <button
                    onClick={addCompany}
                    disabled={!newCompany.name || !newCompany.sector}
                    className="px-6 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors"
                  >
                    Add Company & Compare
                  </button>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default MainComponent;
